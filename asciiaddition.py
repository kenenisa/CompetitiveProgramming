
mat = []
for _ in range(7):
    mat.append(input())
n = len(mat[-1])
lin = []
for i in range(0, n, 6):
    one = []
    for j in range(7):
        for k in range(i,i+5):
            one.append(mat[j][k])
    lin.append("".join(one))
nums = [
    "xxxxxx...xx...xx...xx...xx...xxxxxx",
    "....x....x....x....x....x....x....x",
    "xxxxx....x....xxxxxxx....x....xxxxx",
    "xxxxx....x....xxxxxx....x....xxxxxx",
    "x...xx...xx...xxxxxx....x....x....x",
    "xxxxxx....x....xxxxx....x....xxxxxx",
    "xxxxxx....x....xxxxxx...xx...xxxxxx",
    "xxxxx....x....x....x....x....x....x",
    "xxxxxx...xx...xxxxxxx...xx...xxxxxx",
    "xxxxxx...xx...xxxxxx....x....xxxxxx",
    ".......x....x..xxxxx..x....x......."
]
df ={}
for i in range(10):
    df[nums[i]] = str(i)

num1 = ''
num2 = ''
first = True
for l in lin:
    if l == nums[10]:
        first = False
    else:
        if first:
            num1 += df[l]
        else:
            num2 += df[l]
ans = str(int(num1) + int(num2))

for j in range(7):
    r = []
    for i in range(len(ans)):
        r.append(nums[int(ans[i])][j*5:(j*5)+5])
    print(".".join(r),end="")
    print()

        

