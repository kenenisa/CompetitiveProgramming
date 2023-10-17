

class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None for _ in range(26)]


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            ix = ord(i) - ord('a')
            if not cur.children[ix]:
                cur.children[ix] = TrieNode()
            cur = cur.children[ix]
        cur.isEndOfWord = True
    def dfs(self,i,word,node):
        if not node: return False
        if len(word) == i:
            return node.isEndOfWord
        if word[i] == '.':
            return any([self.dfs(i+1,word,j) for j in node.children])
        else:
            ix = ord(word[i]) - ord('a')
            return self.dfs(i+1,word,node.children[ix])

                
                    

    def search(self, word: str) -> bool:
        return self.dfs(0,word,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)