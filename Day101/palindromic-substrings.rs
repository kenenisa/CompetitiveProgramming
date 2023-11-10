// fastest solution
impl Solution {
    pub fn count_substrings(s: String) -> i32 {
       let mut count:i32 = 0;
       let n = s.len();
       let ss = s.as_bytes();
       for i in 0..n {
           let mut j:usize = 1;
           while i>=j && i+j < n && ss[i-j] == ss[i+j] {
               j+=1;
           }
           count += j as i32;
           if i+1 < n && ss[i] == ss[i+1] {
               j = 1;
               while i>=j && i+j+1 < n && ss[i-j] == ss[i+j+1] {
                   j+=1;
               }
               count += j as i32;
           }
       }
       return count;
    }
}
