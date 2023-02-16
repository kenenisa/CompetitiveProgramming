class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n,m,i,j,result = len(players),len(trainers),0,0,0
        while i < n and j < m:
            if players[i] <= trainers[j]:
                result += 1
                i += 1
                j += 1
            else:
                j+=1
        return result