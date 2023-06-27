n, k = list(map(int, input().split()))
walls = [input(), input()]

def run():
    stack = [((0, 0), 0)]
    visited = set()
    while stack:
        v, time = stack.pop(0)
        x, y = v

        if y >= n:
            return "YES"
        if v not in visited:
            visited.add(v)
            new_x = 1 if x == 0 else 0
            if y + k >= n or walls[new_x][y + k] == '-':
                if (new_x, y + k) not in visited:
                    stack.append(((new_x, y + k),time+1))

            if y + 1 >= n or walls[x][y + 1] == '-':
                if (x, y + 1) not in visited:
                    stack.append(((x, y + 1),time+1))

            if walls[x][y - 1] == '-' and y - 1 > time:
                if (x, y - 1) not in visited:
                    stack.append(((x, y - 1),time+1))

    return "NO"


print(run())
