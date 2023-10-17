n = int(input())
skills = list(map(int, input().split()))
skills.sort()
print(skills[n//2] - skills[n//2 - 1])