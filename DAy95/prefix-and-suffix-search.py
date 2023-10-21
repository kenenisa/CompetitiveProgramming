## EDGES cases
# when prefix and suffix are same
# when there is overlap between prefix and suffix

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word,index):
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.index = index
    def searchPrefix(self,pref):
        cur = self.root
        for i in pref:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return None
        return cur
    def dfs(self,node:TrieNode,find:str,result:List[TrieNode])->List[TrieNode]:
        cur = node
        for k,v in cur.children.items():
            if k == find:
                result.append(cur)
            self.dfs(v,find,result)
        return result
    def searchSuffix(self,nodes:List[TrieNode],suf:str)->int:
        idx = set([-1])
        for node in nodes:
            cur = node
            valid = True
            for i in suf:
                if i in cur.children:
                    cur = cur.children[i]
                else:
                    valid = False
                    break
            if valid: idx.add(cur.index)
        return max(idx)
    def collision(self, p,s):
        result = []
        for i in range(len(p)):
            if p[i] == s[0]:
                j = i
                while j<len(p) and j-i < len(s) and p[j] == s[j-i]:
                    j+=1
                if j == len(p):
                    result.append(p+s[j-i:])
        return result
    def search(self,pref:str,suff:str)->int:
        node = self.searchPrefix(pref)
        if node:
            d =self.dfs(node,suff[0],[])
            if d:
                return self.searchSuffix(d,suff) 
        return -1
        

class WordFilter:
    def __init__(self, words: List[str]):
        self.t = Trie()
        self.lookup = defaultdict()
        for i in range(len(words)):
            self.t.insert(words[i],i)
            self.lookup[words[i]] = i
    
    def f(self, pref: str, suff: str) -> int:
        result = []
        if pref == suff and pref in self.lookup:
            result.append(self.lookup[pref])
        detected = self.t.collision(pref,suff)
        if detected:
            for d in detected: 
                if d in self.lookup: result.append(self.lookup[d])
        result.append(self.t.search(pref,suff))
        return max(result)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
