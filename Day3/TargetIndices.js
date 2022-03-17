/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var targetIndices = function(nums, target) {
    nums.sort(function(x,y){return x - y})
    const newArr = [];
    const n = nums.length
    for(let i = 0; i < n;i++){
        if(nums[i] === target){
            newArr.push(i)
        }
    }
    return newArr
};