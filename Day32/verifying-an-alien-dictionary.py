class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = dict()
        x = 1
        for k in order:
            alphabet[k] = x
            x += 1
        def checkValid(word1,word2):
            v = True
            l = len(word1)
            for i in range(l):
                w1 = alphabet[word1[i]]
                if i == len(word2):
                    v = False
                    break
                w2 = alphabet[word2[i]]
                if w1 < w2:
                    break
                elif w1 > w2:
                    v = False
                    break
            return v
        n = len(words)
        valid = True
        for i in range(1,n):
            if not checkValid(words[i-1],words[i]):
                valid = False
                break
        return valid
            