n=int(input())
p=input().split()
result = []
for i in range(n):
	result.append(p.index(str(i+1))+1)
print(*result)