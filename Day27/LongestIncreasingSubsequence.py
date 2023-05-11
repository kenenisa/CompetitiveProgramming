class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        keep_sorted=[]
        for i in nums:
            insert_position = bisect_left(keep_sorted,i)
            n = len(keep_sorted)
            if insert_position == n:
                keep_sorted.append(i)
            else:
                keep_sorted[insert_position] = i 
        return len(keep_sorted)
