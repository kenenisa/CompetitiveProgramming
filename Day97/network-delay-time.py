class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        df = defaultdict(list)
        for u,v,w in times:
            df[u].append((v,w))
        
        delay = [float('inf')] * n
        delay[k-1] = 0
        h = []
        heappush(h,(0,k))
        while h:
            w,u = heappop(h)
            for v,x in df[u]:
                i = w+x
                if i < delay[v-1]:
                    delay[v-1] = i
                    heappush(h,(i,v))
        if float('inf') in delay:
            return -1
        return max(delay)
        
