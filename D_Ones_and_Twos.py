class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, delta):
        while idx < len(self.bit):
            self.bit[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

t = int(input())
for _ in range(t):
    n,q=list(map(int,input().split()))
    a = list(map(int,input().split()))
    bit = BIT(n)
    prefix_sum = [0] * (n + 1)
    freq = {0: 1}
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
        freq[prefix_sum[i]] = freq.get(prefix_sum[i], 0) + 1
    # Keep track of the number of 1s and 2s in the array
    ones_count = a.count(1)
    twos_count = a.count(2)
    for _ in range(q):
        op = list(map(int,input().split()))
        qt = op[0]
        if qt == 1:
            # Check if there exists a subarray with sum s
            s = op[1]
            # Since the array only contains 1s and 2s, we can check if it's possible to form sum s
            if s <= ones_count + 2 * twos_count and (s <= ones_count or (s - ones_count) % 2 == 0):
                print("YES")
            else:
                print("NO")
        elif qt == 2:
            # Update the value at index i to v
            _,i,v = op
            if a[i - 1] != v:
                # Update the count of 1s and 2s
                if v == 1:
                    ones_count += 1
                    twos_count -= 1
                else:
                    ones_count -= 1
                    twos_count += 1
                # Update the array
                a[i - 1] = v




