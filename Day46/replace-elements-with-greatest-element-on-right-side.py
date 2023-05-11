class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = -1
        for i in range(n-1,-1,-1):
            t = arr[i]
            arr[i]=mx
            mx = max(mx,t)
        return arr
        