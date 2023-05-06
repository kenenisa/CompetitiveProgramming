use std::collections::HashMap;
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut base = 0;
        for n in nums {
            base ^= n;
        }
        base     
    }
}