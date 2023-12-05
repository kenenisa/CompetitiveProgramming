import os

cd = os.getcwd()
with open(os.path.join(cd, 'adventOfCode2023', 'day04.txt'), 'r') as file:
    count = 0
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    df = {"red": 12, "green": 13, "blue": 14}
    cnt = [1]*1000
    cnt[0] = 0
    x = 0
    for line in file:
        line = line.strip()
        x += 1
        nums = line.split(':')[1].strip()
        first, second = nums.split("|")
        f2 = []
        for j in first.strip().split(' '):
            if j.strip():
                f2.append(int(j))
        s2 = []
        for j in second.strip().split(' '):
            if j.strip():
                s2.append(int(j))
        # print(f2,s2)
        c = 0
        for i in f2:
            if i in s2:
                c += 1
        for i in range(x+1, x+1+c):
            cnt[i] += cnt[x]
    # print()
    print(sum(cnt[:x+1]))


# part one
# import os

# cd = os.getcwd()
# with open(os.path.join(cd, 'adventOfCode2023', 'day04.txt'), 'r') as file:
#     count = 0
#     nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
#             'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
#     df = {"red":12,"green":13,"blue":14}
#     for line in file:
#         line = line.strip()
#         nums = line.split(':')[1].strip()
#         first,second = nums.split("|")
#         f2 = []
#         for j in first.strip().split(' '):
#             if j.strip():
#                 f2.append(int(j))
#         s2 = []
#         for j in second.strip().split(' '):
#             if j.strip():
#                 s2.append(int(j))
#         # print(f2,s2)
#         c = 0
#         for i in f2:
#             if i in s2:
#                 if c == 0:
#                     c += 1
#                 else:
#                     c *= 2
#         count += c

#     print(count)
