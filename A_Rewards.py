from math import ceil
print("YES" if ceil(sum(list(map(int, input().split())))/5) + ceil(sum(list(map(int, input().split())))/10) <= int(input()) else "NO")
