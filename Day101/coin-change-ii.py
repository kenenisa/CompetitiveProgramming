class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        choice = [0] * (amount+1)
        choice[0] = 1
        cons = [[] for _ in range(amount+1)]
        for c in coins:
            for i in range(1,amount+1):
                if i-c >= 0 and choice[i-c] > 0:
                    choice[i] += choice[i-c]
        return choice[amount]
