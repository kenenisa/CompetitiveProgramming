#[allow(unused_macros)]
macro_rules! read {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("A String");
        let $out = inner.trim().parse::<$type>().expect("Parsable");
    };
}
 
#[allow(unused_macros)]
macro_rules! read_str {
    ($out:ident) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("A String");
        let $out = inner.trim();
    };
}
 
#[allow(unused_macros)]
macro_rules! read_vec {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).unwrap();
        let $out = inner
            .trim()
            .split_whitespace()
            .map(|s| s.parse::<$type>().unwrap())
            .collect::<Vec<$type>>();
    };
}
#[allow(unused_variables)]
fn main(){
    read!(t as i64);
    for _ in 0..t {
        read_vec!(nm as i64);
        read_vec!(a as i64);
        let mut prefix:Vec<i64> = Vec::new();
        prefix.push(0);
        for i in 0..nm[0] {
            prefix.push(prefix[i as usize] + a[i as usize]);
        }
        let total: i64 = a.iter().sum();
        for _ in 0..nm[1] {
            read_vec!(lrk as i64);
            let amount = (lrk[1] - lrk[0] + 1) * lrk[2];
            let g = (total - (prefix[lrk[1] as usize] - prefix[(lrk[0]-1) as usize])) + amount;
            if g % 2 == 1 {
                println!("YES");
            }else {
                println!("NO");
            }
        }
    }
    
}
