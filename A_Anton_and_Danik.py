n = int(input())
s = input()

c = s.count('A')

if c == n-c:
    print('Friendship')
elif c > n-c:
    print('Anton')
else:
    print('Danik')

