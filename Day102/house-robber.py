impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp:Vec<i32> = Vec::new();
        dp.push(0);
        let mut result: i32 = 0;
        for i in 0..n {
            dp.push(nums[i]);
            if nums[i] > result {
                result = nums[i];
            }
        }
        let mut j = 0;
        for i in 0..n {
            j = 2;
            while i+j <=n {
                if dp[i]+nums[i+j-1] > dp[i+j]{
                    dp[i+j] =  dp[i]+nums[i+j-1];
                }
                if dp[i+j] > result {
                    result = dp[i+j];
                }
                j+=1;
            }
        }
        result
    }
}
