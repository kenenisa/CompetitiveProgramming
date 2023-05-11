class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        result = 0

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                item = stack.pop()
                j = -1
                if stack:
                    j = stack[-1]
                result += (item - j) * (i - item) * arr[item]
            stack.append(i)
        while stack:
            item = stack.pop()
            j = -1
            if stack:
                j = stack[-1]
            result += (item - j) * (n - item) * arr[item]
        return result % (10**9 + 7)
