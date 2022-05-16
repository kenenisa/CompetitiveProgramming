nums = [1,1,2,1,1]
k = 3
n = len(nums)
j = 0
mx = 0
for i in range(n):
    if nums[i] % 2 == 0:  continue #go to the right untill we find zeros
    if k > 0: #exhaust zeros at first
        k -= 1
        continue
    mx = max(mx,i - j)
    while j < i and nums[j] % 2 != 0: #shrink the window from left to right
        j += 1
    j += 1
mx = max(mx,n - j)
print(mx)