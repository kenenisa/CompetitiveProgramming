class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pref = []
        n = len(nums)
        m = nums[0]
        pref.append(m)
        for i in range(1,n):
            pref.append(m)
            m = min(nums[i],m)
        suf = []
        m = nums[-1]
        suf.append(m)
        for i in range(n-2,-1,-1):
            suf.append(m)
            m = max(nums[i],m)
        suf.reverse()
        for j in range(1,n-1):
            if pref[j] < nums[j] < suf[j]:
                return True
        return False 
            
        
