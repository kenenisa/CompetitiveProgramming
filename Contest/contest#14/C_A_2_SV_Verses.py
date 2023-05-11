n,a,b=list(map(int,input().split()))
al = list(map(int,input().split()))
def count(nums, x):
	s = 0
	result = 0
	left = 0
	right = 0
	while right < n :
		s += nums[right]
		while left <= right and s > x:
			s -= nums[left]
			left += 1
		result += right - left + 1
		right += 1
	return result
print(count(al, b) - count(al,a-1))