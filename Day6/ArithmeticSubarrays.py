class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        il = len(l)
        for k in range(il):
            temp = sorted(nums[l[k]:r[k]+1])
            val = True
            diff = temp[0] - temp[1]
            tl = len(temp) - 1
            for j in range(1,tl):
                if(diff != (temp[j] - temp[j + 1])):
                    val = False
                    break
            result.append(val)
        return result
        