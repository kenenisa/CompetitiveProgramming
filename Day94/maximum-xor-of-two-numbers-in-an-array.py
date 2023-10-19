class TrieNode:
    def __init__(self):
        self.value = 0
        self.one = None
        self.zero = None
        

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        root = TrieNode()
        for num in nums:
            cur = root
            for i in range(31,-1,-1):
                if num & (1<<i):
                    if not cur.one:
                        cur.one = TrieNode()
                    cur = cur.one
                else:
                    if not cur.zero:
                        cur.zero =  TrieNode()
                    cur = cur.zero
            cur.value = num
        result = 0
        for num in nums:
            cur = root
            for i in range(31,-1,-1):
                if num & (1 << i):
                    if cur.zero:
                        cur = cur.zero
                    else:
                        if cur.one:
                            cur = cur.one
                else:
                    if cur.one:
                        cur = cur.one
                    else:
                        if cur.zero:
                            cur = cur.zero
            result = max(result,num^cur.value)
        return result
        
