class TrieNode:
    def __init__(self):
        self.words = []
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
            cur.words.append(word)
    def search(self,pref:str):
        cur = self.root
        for i in pref:
            if i not in cur.children:
                return []
            cur = cur.children[i]
        return cur.words
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        for p in products:
            t.insert(p)
        result = []
        for i in range(len(searchWord)):
            searched = t.search(searchWord[:i+1])
            searched.sort()
            result.append(searched[:3])
        return result

        
