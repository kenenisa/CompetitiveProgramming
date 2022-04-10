class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dp = [0] * (len(nums) + 1)

        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + nums[i - 1]
        n = len(nums) + 1
        Queue = deque()

        for i in range(len(dp)):
            while Queue and dp[i] - dp[Queue[0]] >= k:
                n = min(n, i - Queue.popleft())
            while Queue and dp[i] < dp[Queue[-1]]:
                Queue.pop()
            Queue.append(i)
        return n if n != len(nums)+1 else -1