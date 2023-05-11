/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var smallerNumbersThanCurrent = function(nums) {
    const n = nums.length
   const result = []
   for (let i = 0; i < n; i++) {
       for (let j = 0; j < n; j++) {
           const rv = result[i] === undefined
           if (nums[j] < nums[i]) {
               if (rv) {
                   result[i] = 1
               } else {
                   result[i] += 1
               }
           } else {
               if (rv) {
                   result[i] = 0
               }
           }
       }
   }
   return result
};