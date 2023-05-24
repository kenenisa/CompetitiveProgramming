n = input()
magic = ["1","14","144"]

def dfs(s):
    if s == n:
        return True
    if len(s) > len(n):
        return False
    return dfs(s+magic[0]) or dfs(s+magic[1]) or dfs(s+magic[2])

print("YES" if dfs("") else "NO")