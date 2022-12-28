# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0
        
        prefix = ""
        while True:
            try:
                lastItem = strs[0][k]
                for i in strs:
                    if i[k] != lastItem:
                        1/0
                prefix += lastItem
                k+=1
            except:
                break
        return prefix