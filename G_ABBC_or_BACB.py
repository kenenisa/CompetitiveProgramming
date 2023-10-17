t = int(input())
for _ in range(t):
    inp = input()
    print(inp.count('A') - min(map(len, inp.split('B'))))
