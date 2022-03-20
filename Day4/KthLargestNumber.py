class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def ConvertToInt(el):
            return int(el)
        nums.sort(key=ConvertToInt)
        return nums[-k]