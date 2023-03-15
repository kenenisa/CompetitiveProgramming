class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        items = {}
        n = len(fruits)
        j = 0
        mx = 0
        for i in range(n):
            if items.get(fruits[i]):
                items[fruits[i]] += 1
            else:
                items[fruits[i]] = 1
            mx = max(mx,i - j)
            if len(items) > 2:
                while len(items) > 2 and j < i:
                    items[fruits[j]] -= 1
                    if items[fruits[j]] < 1:
                        items.pop(fruits[j])
                    j += 1
        mx = max(mx,n - j)
        return mx