t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    prefix = [0]
    for aa in a:
        prefix.append(prefix[-1] + aa)

    left = 0
    right = n - 1
    def ask(l,r):
        print("?",r - l,end=" ")
        for i in range(l,r+1):
            print(i,end=" ")
        print()
    while left < right:
        mid = (right + left) // 2

        # check if left is valid
        ask(left,mid)
        m = int(input())
        mass = prefix[mid] - prefix[left-1]
        if m > mass:
            right = mid - 1
            continue
        # check if right is valid
        ask(mid,right)
        m = int(input())
        mass = prefix[right] - prefix[mid-1]
        if m > mass:
            left = mid + 1
            continue
    print("!",left)
    stdout.flush()
