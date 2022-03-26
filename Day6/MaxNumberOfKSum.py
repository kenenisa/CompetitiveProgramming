from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        obj = defaultdict(int)
        result = 0
        for i in range(len(nums)):
            j = k - nums[i]
            if(obj[j] == 0):
                obj[nums[i]] += 1
            else:    
                result +=1
                obj[j] -= 1

        return result
        