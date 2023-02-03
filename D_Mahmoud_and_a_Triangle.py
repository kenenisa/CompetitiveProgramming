n = int(input())
nums = list(map(int,input().split()))
nums.sort()
def the(n,nums):
    for i in range(n - 1, 0, -1):
        l = 0
        r = i - 1
        while(l < r):
            if nums[l] + nums[r] > nums[i]:
                return "YES"
            l += 1
    return "NO"
print(the(n,nums))

 