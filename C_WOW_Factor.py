s = input()

countV = 0
result = []
for l in s:
    if l == 'v':
        countV += 1
    else:
        for _ in range(1,countV):
            result.append('w')
        countV = 0
        result.append('o')
for _ in range(1,countV):
    result.append('w')
dp = [0] * (len(result)+1)

ws= 0
count= 0
for i in range(1,len(result)+1):
    dp[i] += dp[i-1]
    if result[i-1] == 'w':
        dp[i] += 1
        count += ws
    else:
        ws += dp[i]
print(count)

