class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        Qmax = deque()
        Qmin = deque()
        result = 0
        x = 0

        for r in range(len(nums)):
            while Qmax and nums[Qmax[-1]] < nums[r]:
                Qmax.pop()
            Qmax.append(r)
            while Qmin and nums[Qmin[-1]] > nums[r]:
                Qmin.pop()
            Qmin.append(r)

            mx = nums[Qmax[0]]
            mi = nums[Qmin[0]]
            if abs(mx - mi) <= limit:
                result = max(result, r-x+1)
            else:
                # shrink window
                if x == Qmax[0]:
                    Qmax.popleft()
                if x == Qmin[0]:
                    Qmin.popleft()
                x += 1
        return result