class TrieNode:
    def __init__(self):
        self.value = 0
        self.zero = None
        self.one = None
        self.count = 0
t = int(input())
root = TrieNode()
for _ in range(t):
    sign, num = input().split()
    num = int(num)
    if sign == '+':
        cur = root
        for i in range(31,-1,-1):
            if num & (1 << i):
                if not cur.one:
                    cur.one = TrieNode()
                cur = cur.one
            else:
                if not cur.zero:
                    cur.zero = TrieNode()
                cur = cur.zero
            cur.count += 1
        cur.value = num
    elif sign == '-':
        cur = root
        for i in range(31,-1,-1):
            if num & (1 << i):
                cur = cur.one
            else:
                cur = cur.zero
            cur.count -= 1
    else:
        cur = root
        for i in range(31,-1,-1):
            if num & (1 << i):
                if cur.zero and cur.zero.count:
                    cur = cur.zero
                elif cur.one and cur.one.count:
                    cur = cur.one
            else:
                if cur.one and cur.one.count:
                    cur = cur.one
                elif cur.zero and cur.zero.count:
                    cur = cur.zero

        print(max(num, num^cur.value))
