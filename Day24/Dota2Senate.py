class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r = deque()
        d = deque()
        
        for i,x in enumerate(senate):
            if x == "R":
                r.append(i)
                continue
            d.append(i)
                
        while r and d:
            if r[0] < d[0]:
                r.append(r.popleft()+n)
                d.popleft()
                continue
            r.popleft()
            d.append(d.popleft() + n)
        
        return "Radiant" if r else "Dire"
