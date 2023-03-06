class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        target = [0] * 26
        df = [0] * 26
        np = len(p)
        n = len(s)
        if np > n:
            return []
        for i in range(np):
            target[ord(p[i]) - 97] += 1
            df[ord(s[i]) - 97] += 1
        result = []
        while left < n - np:
            if target == df:
                result.append(left)
            df[ord(s[left]) - 97] -= 1
            df[ord(s[left + np]) - 97] += 1
            left += 1
        if target == df:
            result.append(left)
        return result


            
