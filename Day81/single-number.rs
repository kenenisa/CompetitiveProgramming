use std::collections::HashMap;
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut df: HashMap<i32,i32> = HashMap::new();
        for i in 0..nums.len() {
           if let Some(item) = df.get(&nums[i]){
               df.insert(nums[i],item+1);
           }else{
               df.insert(nums[i],1);
           }
        }
        for (key, value) in df.iter() {
            if *value == 1 {
                return *key;
            }
        }
        return 0;
        
    }
}