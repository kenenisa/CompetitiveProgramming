class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        root = TrieNode()
        for word in words:
            cur = root
            for i in word:
                if i not in cur.children:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            cur.end = True
        self.result = []
        def dfs(node,word):
            if node.end:
                self.result.append(word)
                if node.children:
                    for k,v in node.children.items():
                        dfs(v,word+k)
        for k,v in root.children.items():
            dfs(v,k)
        if self.result:
            def compare(a,b):
                if len(a) == len(b):
                    if a < b:
                        return -1
                    return 1
                return len(b) - len(a)
            self.result.sort(key=cmp_to_key(compare))
            return self.result[0]
        return ""
                

        
          
        
