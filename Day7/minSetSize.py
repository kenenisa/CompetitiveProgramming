#puts it into a dict then subtracts the most frequent elements from half of the input list
from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)/2
        df = defaultdict(int)
        result = []
        for i in arr:
            df[i] += 1
        df = sorted(df.items(),key=lambda k:k[1],reverse=True)
        for j,k in df:
            if(n > 0):
                n = n - k
                result.append(j)
        l = len(result)
        return l if l>0 else 1