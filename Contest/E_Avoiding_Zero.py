def rearrange_array(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1:]
        b = sorted(a, key=lambda x: abs(x))[::-1]

        if sum(a) == 0:
            print("NO")
        else:
            print("YES")
            pos, neg = [], []
            for num in b:
                if num > 0:
                    pos.append(num)
                else:
                    neg.append(num)
            pos_count, neg_count = 0, 0
            result = []
            for j in range(len(b)):
                if (j % 2 == 0 and pos_count < len(pos)) or neg_count >= len(neg):
                    result.append(pos[pos_count])
                    pos_count += 1
                else:
                    result.append(neg[neg_count])
                    neg_count += 1
            print(*result)

t = int(input().strip())
test_cases = []
for i in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    test_cases.append([n] + a)
rearrange_array(t, test_cases)


