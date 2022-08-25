class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0: return True
        q = deque()
        visited = set()
        q.append(start)
        n = len(arr)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if arr[node] == 0: return True
                nxt = node+arr[node]
                prev = node-arr[node]
                if nxt < n and (nxt,'+') not in visited: 
                    visited.add((nxt,'+'))
                    q.append(nxt)                
                if prev >= 0 and (prev,'-') not in visited: 
                    visited.add((prev,'-'))
                    q.append(prev)
        return False
        
        
