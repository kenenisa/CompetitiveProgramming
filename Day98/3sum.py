class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        c = Counter(nums)
        n = len(nums)
        used = set()
        result = []
        for i in range(n):
            for j in range(i+1,n):
                m = -1 * (nums[i] + nums[j]) 
                if m in s:
                    a = 0
                    if m == nums[i]:
                        a+=1
                    if m == nums[j]:
                        a+=1
                    b = c[m] > a

                    if b:
                        r = [nums[i],nums[j],m]
                        r.sort()
                        b = "-".join(map(str,r))
                        if b not in used:
                            used.add(b)
                            result.append(r)
        return result
                
        
