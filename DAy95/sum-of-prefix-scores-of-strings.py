class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
            cur.count += 1
    def search(self,word:str)->int:
        # print(word)
        cur = self.root
        result = 0
        for i in word:
            cur = cur.children[i]
            result += cur.count
        return result

    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        for word in words:
            t.insert(word)
        result = []
        for word in words:
            l = 0
            result.append(t.search(word))

        return result
