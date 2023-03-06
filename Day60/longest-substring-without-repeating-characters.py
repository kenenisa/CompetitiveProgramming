class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dt = deque()
        size = 0
        n = len(s)
        for i in range(n):
            while dt and s[i] in dt:
                dt.popleft()
            dt.append(s[i])
            size = max(size,len(dt))
        return size
            
