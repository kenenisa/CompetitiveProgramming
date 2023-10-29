class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        df = defaultdict(list)
        for i in range(len(edges)):
            u,v = edges[i]
            df[u].append((v,succProb[i]))
            df[v].append((u,succProb[i]))
        
        prob = [float('-inf')] * n
        prob[start_node] = 1
        h = []
        heappush(h,(-1,start_node))
        while h:
            p,node = heappop(h)
            p *= -1
            if node == end_node:
                return p
            for u,pp in df[node]:
                if p * pp > prob[u]:
                    prob[u] = p * pp
                    heappush(h,(- p * pp,u))
        return 0
