class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        result = 0
        vowels ='aeiou'
        for i in range(n):
            if word[i] in vowels:
                result += (n - i) * (i + 1)
        return result