class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        p1 = 0
        p2 = 0
        result = []
        n , m = len(word1) , len(word2)

        while(p1 < n and p2 < m ):
            if word1[p1:] >= word2[p2:]:
                result.append(word1[p1])
                p1 += 1
            else:
                result.append(word2[p2])
                p2 += 1
        return ''.join(result) + word1[p1:] + word2[p2:]