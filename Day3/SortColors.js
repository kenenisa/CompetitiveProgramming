/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var sortColors = function(nums) {

    const n = nums.length
    for(let i = 0; i < n;i++){
        for(let j = 0; j < n;j++){
            if(nums[i] < nums[j]){
                const t = nums[i];
                nums[i] = nums[j];
                nums[j] = t
            }
        }
    }
};