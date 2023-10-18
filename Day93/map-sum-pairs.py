class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = [None for _ in range(26)]
class MapSum:

    def __init__(self):
        self.root = TrieNode(0)
        self.visited = {}
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for i in key:
            ix = ord(i) - ord('a')
            if not cur.children[ix]:
                cur.children[ix] = TrieNode(val)
            else:
                if key in self.visited:
                    cur.children[ix].val -= self.visited[key]
                cur.children[ix].val += val
            cur = cur.children[ix]
        self.visited[key] = val
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for p in prefix:
            ix = ord(p) - ord('a')
            if not cur.children[ix]:
                return 0
            cur = cur.children[ix]
        return cur.val
            

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
