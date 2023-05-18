class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1

        result = []
        def dfs(item,path):
            if item == n:
               result.append(path[::])
            else:
                for x in graph[item]:
                    path.append(x)
                    dfs(x,path)
                    path.pop()

        dfs(0,[0])
        return result