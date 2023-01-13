class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        df = defaultdict(int)
        for i in range(len(nums)):
            df[nums[i]] = i
        for op in operations:
            if op[0] in df:
                nums[df[op[0]]] = op[1]
                df[op[1]] = df.pop(op[0])
        return nums