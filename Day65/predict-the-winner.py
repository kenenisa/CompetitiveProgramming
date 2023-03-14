class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(start, end):
            if start == end :
                return nums[start]
            return max(nums[start] - winner(start+1, end), nums[end] - winner(start, end-1)) # consider every route
        return winner(0,len(nums)-1) >= 0