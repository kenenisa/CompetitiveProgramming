class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None for _ in range(26)]
        self.count = 0
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        self.result = 0
        def dfs(node,word,j):
            if node.end:
               self.result += node.count
            for i in range(26):
                if node.children[i]:
                    for k in range(j,len(word)):
                        if chr(ord('a')+i) == word[k]:
                            dfs(node.children[i],word,k+1)
                            break
        root = TrieNode()
        for word in words:
            cur = root
            for i in word:
                ix = ord(i) - ord('a')
                if not cur.children[ix]:
                    cur.children[ix] = TrieNode()
                cur = cur.children[ix]
            cur.end = True
            cur.count += 1
        dfs(root,s,0)
        return self.result
        
            

        
