from sys import stdin, stdout
input = stdin.readline

t = int(input())
for _ in range(t):
    n,q=list(map(int,input().split()))
    a = list(map(int,input().split()))
    x = list(map(int,input().split()))  
    # Create a prefix sum array
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + a[i-1]

    # Create a segment tree
    seg_tree = [0] * (4*n)

    def build_tree(node, start, end):
        if start == end:
            seg_tree[node] = a[start]
        else:
            mid = (start + end) // 2
            build_tree(2*node, start, mid)
            build_tree(2*node+1, mid+1, end)
            seg_tree[node] = max(seg_tree[2*node], seg_tree[2*node+1])

    build_tree(1, 0, n-1)

    # Perform the modifications
    for xi in x:
        power = 2 ** xi
        half_power = power // 2

        while seg_tree[1] >= power:
            # Find the rightmost index with value >= power
            node = 1
            start = 0
            end = n-1

            while start != end:
                mid = (start + end) // 2
                if seg_tree[2*node] >= power:
                    node = 2*node
                    end = mid
                else:
                    node = 2*node+1
                    start = mid+1

            idx = start

            # Update the segment tree
            a[idx] += half_power
            seg_tree[node] += half_power
            node //= 2
            while node:
                seg_tree[node] = max(seg_tree[2*node], seg_tree[2*node+1])
                node //= 2

    print(*a)
