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
    read_vec!(b as i32);
    let n: i32 = b[0];
    let k: i32 = b[1];
    let q: i32 = b[2];
    let mut c: Vec<i32> = vec![0; 200002];
    for i in 0..n {
        read_vec!(a as usize);
        c[a[0]] += 1;
        c[a[1] + 1] -= 1;
    }
    for i in 1..c.len() {
        c[i] += c[i - 1];
    }
    for i in 1..c.len(){
        if c[i] >= k {
            c[i] = c[i-1] + 1;
        }else{
            c[i] = c[i-1];
        }
    }
    for i in 0..q {
        read_vec!(d as usize);
        println!("{:?}",c[d[1]] - c[d[0]-1]);
    }
}

// python too SLOW

// n,k,q=list(map(int,input().split()))
// c = [0]*200002
// for _ in range(n):
//     l,r=list(map(int,input().split()))
//     c[l] += 1
//     c[r+1] -= 1
// for i in range(1,200002):
//     c[i] += c[i-1]
 
// for i in range(1,200002):
//     if c[i] >= k:
//         c[i] = c[i-1] + 1
//     else:
//         c[i] = c[i-1]
// # for i in range(1,200002):
// #     c[i] += c[i-1]
 
// result = []
// for _ in range(q):
//     a,b=list(map(int,input().split()))
//     print(c[b] - c[a-1])
