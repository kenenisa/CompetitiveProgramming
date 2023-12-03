# part two
import os
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
]
cd = os.getcwd()
with open(os.path.join(cd, 'adventOfCode2023', 'day03.txt'), 'r') as file:
    count = 0
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    df = {"red": 12, "green": 13, "blue": 14}
    grid = []
    for line in file:
        line = line.strip()
        grid.append(line)
    n = len(grid)
    m = len(grid[0])
    parts = []
    df = {}
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            part = []
            f = ''
            while j < m and grid[i][j] in '0987654321':
                part.append((i, j))
                f += grid[i][j]
                j += 1
            j += 1
            if part:
                for p in part:
                    df[p] = int(f)
    def checker(part):
        i, j = part
        nums = set()
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            if 0 <= x < n and 0 <= y < m and grid[x][y] in '0987654321':
                nums.add(df[(x, y)])
        if len(nums) == 2:
            p = 1
            for i in nums:
                p *= i
            return p
        return 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                count += checker((i,j))
    print(count)


# part one
# import os
# directions = [
#     (1, 0),
#     (-1, 0),
#     (0, 1),
#     (0, -1),
#     (-1, -1),
#     (1, 1),
#     (-1, 1),
#     (1, -1),
# ]
# cd = os.getcwd()
# with open(os.path.join(cd, 'adventOfCode2023', 'day03.txt'), 'r') as file:
#     count = 0
#     nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
#             'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
#     df = {"red": 12, "green": 13, "blue": 14}
#     grid = []
#     for line in file:
#         line = line.strip()
#         grid.append(line)
#     n = len(grid)
#     m = len(grid[0])
#     parts = []
#     for i in range(len(grid)):
#         j = 0
#         while j < len(grid[i]):
#             part = []
#             while j < m and grid[i][j] in '0987654321':
#                 part.append((i, j))
#                 j += 1
#             j += 1
#             if part:
#                 parts.append(part)

#     def checker(part):
#         for i, j in part:
#             for dx, dy in directions:
#                 x = i + dx
#                 y = j + dy
#                 if 0 <= x < n and 0 <= y < m and grid[x][y] not in '0987654321.':
#                     return True
#         return False
#     for part in parts:
#         if checker(part):
#             f = ''
#             for i, j in part:
#                 f += grid[i][j]
#             count += int(f)
#     print(count)
