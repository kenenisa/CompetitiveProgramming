class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1,n+1))
        def play(ary,n,l):
            if len(ary) == 1:  return ary[0]
            turn = (l % n) - 1
            ary.pop(turn)
            l = turn + k if turn != -1 else k
            n -= 1
            return play(ary,n,l)
        return play(players,n,k)