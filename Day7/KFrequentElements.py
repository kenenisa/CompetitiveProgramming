from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        df = defaultdict(int)
        for i in nums:
            df[i] += 1
        df = sorted(df.items(),key=lambda k:k[1],reverse=True)
        result = []
        for j,v in df:
            if(k == 0):
                break
            result.append(j)
            k -= 1
        return result