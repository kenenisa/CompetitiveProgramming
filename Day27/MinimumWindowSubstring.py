class Solution:
	def minWindow(self, s: str, t: str) -> str:
		hash_map = {}
		for c in t:
			hash_map[c] = hash_map.get(c, 0) + 1
		l = r = 0
		n = len(t)
		valid = 0
		minLen = len(s) + 1
		result = ''

		for r in range(len(s)):
			if s[r] in hash_map:
				if hash_map[s[r]] > 0:
					valid += 1
				hash_map[s[r]] -= 1

			while valid >= n:
				if (r - l) + 1 < minLen:
					result = s[l:r+1]
					minLen = (r-l) + 1

				if s[l] in hash_map:
					hash_map[s[l]] += 1
					if hash_map[s[l]] > 0:
						valid -= 1
				l += 1

		return result
#first attempt
# class Solution2:
#     def firstReplace(self,word,ch_to_remove):
#         result = ""
#         occurred_flag = False
#         for ch in word:
#             if ch == ch_to_remove and occurred_flag == False:
#                 occurred_flag = True
#                 continue
#             else:
#                 result += ch
#         return result
#     def validate(self,s,t):
#         temp = s
#         for i in t:
#             if i in temp:
#                 temp = self.firstReplace(temp,i)
#             else:
#                 return False
#         return True
                
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s): return ""
#         r = 0
#         l = 0
#         n = len(s)
#         ans = [0,n+1]
#         while l < n:
#             temp = t
#             while temp != "" and r < n:
#                 if s[r] in temp:
#                     temp = self.firstReplace(temp,s[r])
#                 r += 1
#             temp = t
#             print(s[l:r],r)
#             while l < n and l+1 < n and self.validate(s[l + 1:r],t):
#                 l += 1
#             sliced = s[l:r]
#             print(sliced,r)
#             if len(t) <= len(sliced) < ans[1] - ans[0]:
#                 if self.validate(sliced,t):
#                     ans = [l,r]
#             if r == n:
#                 l += 1
#         if ans[1] - ans[0] > n:
#             return ""
#         return s[ans[0]:ans[1]]
        
