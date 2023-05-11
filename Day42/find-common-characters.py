class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        al = [[0] * 26 for _ in range(n)]
        offset = ord('a')
        for i in range(n):
            for letter in words[i]:
                al[i][ord(letter) - offset] += 1
        result = []
        for i in range(26):
            val = al[0][i]
            if val == 0:
                continue
            valid = True
            for j in range(1,n):
                if al[j][i] == 0:
                    valid = False
                    break
                else:
                    val = min(val,al[j][i])
            if valid:
                for _ in range(val):
                    result.append(chr(offset + i))
        return result
