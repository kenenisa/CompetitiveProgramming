from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)
        ans1 = []
        ans2 = []
        for win,loss in matches:
            winners[win] += 1
            losers[loss] += 1
        for i,x in winners.items():
            if losers[i] == 0:
                ans1.append(i)
        for i,x in losers.items():
            if losers[i] == 1:
                ans2.append(i)
        ans1.sort()
        ans2.sort()
        return [ans1,ans2]