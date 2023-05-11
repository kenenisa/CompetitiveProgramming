class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        ppl = deque(sorted(people))
        while len(ppl) > 1:
            last = ppl[-1]
            boats += 1
            if last == limit or last + ppl[0] > limit:
                ppl.pop()
                continue
            ppl.pop()
            ppl.popleft()
        if len(ppl):
            boats += 1
            ppl.pop()
        return boats
        
