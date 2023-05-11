class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        explored = set()
        df = {i:[] for i in range(len(isConnected))}
        province = 0

        def dfs(node,explored):
            if node in explored:
                return False
            explored.add(node)
            for n in df[node]:
                dfs(n,explored)
            return True
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j] == 1:
                    df[i].append(j)
                    
        for i in df:
            if dfs(i,explored):
                province+=1
        return province
