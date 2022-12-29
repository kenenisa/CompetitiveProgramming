class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = []
        for i in words:
            sets.append(set(i))
        result = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1,n):
                if sets[i] == sets[j]:
                    result += 1
        return result