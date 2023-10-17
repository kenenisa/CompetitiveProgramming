class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word:str) -> None:
        cur = self.root
        for i in word:
            ix = ord(i) - ord('A')
            if not cur.children[ix]:
                cur.children[ix] = TrieNode()
            cur = cur.children[ix]
        cur.validWord = True
                
    
class TrieNode():
    def __init__(self):
        self.validWord = False
        self.children = [None for _ in range(26)
                         
t = Trie()
t.insert("CAT")      
t.insert("CAR")
t.insert("BLACK")
t.insert("BACK")   
