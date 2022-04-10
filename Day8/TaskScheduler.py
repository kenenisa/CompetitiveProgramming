from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        df = collections.defaultdict(int)
        mx = 0
        for task in tasks:
            df[task] += 1
            mx = max(mx, df[task])

        result = (mx-1) * (n+1)
        for df in df.values():
            if df == mx:
                result += 1
        return max(result, len(tasks))