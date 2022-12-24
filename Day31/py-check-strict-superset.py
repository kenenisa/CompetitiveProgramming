# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
n = int(input())
result = True
for _ in range(n):
    s = set(input().xsplit())
    if not a.issuperset(s):
        result = False
        break
print(result)