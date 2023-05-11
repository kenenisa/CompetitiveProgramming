impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
         if x == 1{
            return 1;
        }
        let mut left: f64 = 0 as f64;
        let mut right:f64 = x as f64;
        while left < right{
            let mut middle: f64 = (right + left)/2.0;
            let val:f64 = middle * middle;
            if (val as i64) == x as i64{
                return middle as i32;
            }else if val < x as f64{
                left = middle;
            }else{
                right = middle;
            }
        }
        return 0;
    }
}