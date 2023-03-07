class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len (s1) > len(s2):
            return False
        left = 0
        target = [0]*26
        for s in s1:
            target[ord(s)-97] += 1
        window = [0]*26
        for right in range(len(s2)):
            window[ord(s2[right])-97] += 1

            while window[ord(s2[right])-97] > target[ord(s2[right])-97]:
                window[ord(s2[left])-97] -= 1
                left += 1
            if target == window:
                return True
        return False