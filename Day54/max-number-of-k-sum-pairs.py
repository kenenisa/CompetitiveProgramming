from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        obj = defaultdict(int)
        result = 0
        for i in nums:
            j = k - i
            if(obj[j] == 0):
                obj[i] += 1
            else:    
                result +=1
                obj[j] -= 1

        return result
        
