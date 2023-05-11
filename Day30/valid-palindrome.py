# with two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n - i - 1]:
                return False
        return True
# fastest
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
#         return s == s[::-1]