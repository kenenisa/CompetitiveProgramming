n = int(input())
a = list(map(int,input().split()))
mx = 0
result = []
prev = 0
for i in range(n):
	t = [0 for _ in range(n)]
	b = a[i]
	t[i] = b
	last = b
	for j in range(i-1,-1,-1):
		last = min(last,a[j])
		t[j] = last
		b += last
	fromi = a[i]
	for j in range(i+1,n):
		fromi = min(fromi,a[j])
		t[j] = fromi
		b += fromi
	if b > prev:
		result = []
		for i in range(n):
			result.append(t[i])
		prev = b
print(*result)