import os

cd = os.getcwd()
# with open(os.path.join(cd,'adventOfCode2023','day01.txt'), 'r') as file:
#     count = 0
#     for line in file:
#         first = False
#         last = False
#         for i in line:
#             if i in '0987654321':
#                 if not first:
#                     first = last = i
#                 else:
#                     last = i
#         count += int(first+last)
#     print(count)
# part 2
with open(os.path.join(cd, 'adventOfCode2023', 'day01.txt'), 'r') as file:
    count = 0
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    for line in file:
        line = line.strip()
        first = False
        last = False
        for i in range(len(line)):
            ltr = False
            if line[i] in '0987654321':
                ltr = line[i]
            else:
                for j in [3,4,5]:
                    l = line[i:i+j]
                    if l in nums:
                        ltr = nums[l]
                        break
            if ltr:
                if not first:
                    first = last = ltr
                else:
                    last = ltr
        count += int(first+last)
    print(count)
