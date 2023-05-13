a = input()
b = input()
n = len(a)
result = ['0'] * n
for i in range(n):
    if a[i] != b[i]:
        result[i] = '1'
print("".join(result))