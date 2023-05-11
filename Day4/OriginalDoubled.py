from collections import defaultdict

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cd = defaultdict(int)
        for x in changed:
            cd[x] += 1
        changed.sort()
        result = list()
        for x in changed:
            while cd[x] > 0:
                cd[x] -= 1
                try:
                    cd[x * 2] -= 1
                except IndexError:
                    return []
                if cd[x * 2] < 0:
                    return []
                result.append(x)

        return result