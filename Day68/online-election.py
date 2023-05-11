class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.p = persons
        self.t = times
        self.tn = len(times)
        self.results = {}
        
        last = persons[0]
        votes = {}
        mx = 1
        
        for i in range(len(persons)):
            if votes.get(persons[i]):
                votes[persons[i]] += 1
            else:
                votes[persons[i]] = 1
            if votes[persons[i]] >= mx:
                last = persons[i]
                mx = votes[persons[i]]
            self.results[i] = last
            
    def binarySearch(self,t,start,end):
        if self.t[end] <= t and start == end - 1: 
            return end
        middle = int((start + end) / 2)
        if self.t[middle] == t:
            return middle
        if self.t[middle] < t and self.t[middle+1] > t:
            return middle
        
        if self.t[middle] > t:
            return self.binarySearch(t,start, middle)
        return self.binarySearch(t,middle, end)
    def q(self, t: int) -> int:
        return self.results[self.binarySearch(t,0,self.tn-1)]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)