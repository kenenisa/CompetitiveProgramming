n = int(input())
ss = input()
result = 0
for s in ss:
    if s == "-":
        if result > 0:
            result -= 1
    else:
        result += 1
if result < 0:
    print("0")
else:
    print(result)