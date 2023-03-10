class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        n = len(nums) + 1
        Queue = deque()

        for i in range(len(prefix)):
            while Queue and prefix[i] - prefix[Queue[0]] >= k:
                n = min(n, i - Queue.popleft())
            while Queue and prefix[i] < prefix[Queue[-1]]:
                Queue.pop() # pop right
            Queue.append(i)
        return n if n != len(nums)+1 else -1