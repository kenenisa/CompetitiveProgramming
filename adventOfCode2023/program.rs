use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::sync::{Arc, Mutex};
use std::thread;

fn main() -> io::Result<()> {
    let file = File::open("day05.txt")?;
    let reader = io::BufReader::new(file);

    let mut looking_for = Vec::new();
    let mut nxt = Vec::new();
    let mut last = String::from("seed");
    let mut df: HashMap<String, Vec<Vec<u32>>> = HashMap::new();
    let mut index = Vec::new();

    for line in reader.lines() {
        let line = line?;
        if line.is_empty() {
            continue;
        } else if line.starts_with("seeds") {
            nxt = line
                .split(':')
                .nth(1)
                .unwrap()
                .trim()
                .split_whitespace()
                .map(|s| s.parse::<u32>().unwrap())
                .collect();
        } else if line.chars().next().unwrap().is_numeric() {
            df.get_mut(&last).unwrap().push(
                line.split_whitespace()
                    .map(|s| s.parse::<u32>().unwrap())
                    .collect(),
            );
        } else {
            last = line.split_whitespace().next().unwrap().to_string();
            df.insert(last.clone(), Vec::new());
            index.push(last.clone());
        }
    }
    println!("{}", "TOOK INPUT");

    for i in (0..nxt.len()).step_by(2) {
        looking_for.extend(nxt[i]..nxt[i] + nxt[i + 1]);
    }
    println!("{}", "EXTENDED THE INPUT");

    // Wrap looking_for in Arc<Mutex<>> for safe concurrent access
    let looking_for = Arc::new(Mutex::new(looking_for));

    // Create a vector to store thread handles
    let mut handles = vec![];

    for ind in &index {
        let looking_for_clone = Arc::clone(&looking_for);
        let df_clone = df.clone();
        let ind_clone = ind.clone();

        // Spawn a new thread for each index
        let handle = thread::spawn(move || {
            let mut visited = Vec::new();
            let mut transform = HashMap::new();
            println!("{:?}", ind_clone);

            for v in &df_clone[&ind_clone] {
                let d = v[0];
                let s = v[1];
                let r = v[2];
                println!("{:?}", (d, s, r));

                for i in 0..looking_for_clone.lock().unwrap().len() {
                    let l = looking_for_clone.lock().unwrap()[i];
                    if l >= s {
                        let diff = l - s;
                        if l >= s && diff < r {
                            transform.insert(i, d + diff);
                            visited.push(i);
                        }
                    }
                }
            }

            let mut nxt = Vec::new();
            for i in 0..looking_for_clone.lock().unwrap().len() {
                if visited.contains(&i) {
                    nxt.push(*transform.get(&i).unwrap());
                } else {
                    nxt.push(looking_for_clone.lock().unwrap()[i]);
                }
            }
            println!("{:?} FINISHED", ind_clone);

            // Update looking_for using the Mutex
            *looking_for_clone.lock().unwrap() = nxt;
        });

        handles.push(handle);
    }

    // Wait for all threads to finish
    for handle in handles {
        handle.join().unwrap();
        println!("Thread joined");
    }

    println!("{}", looking_for.lock().unwrap().iter().cloned().min().unwrap());

    Ok(())
}
