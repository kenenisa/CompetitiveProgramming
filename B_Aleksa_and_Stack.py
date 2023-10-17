t = int(input())
for _ in range(t):
    n = int(input())
    result = [1]
    while len(result) < n:  
        result.append(result[-1] + 2)
    print(*result)

    

