# from collections import defaultdict
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = input()
#     seen_left = defaultdict(int)
#     prefix_sum = []
#     acc = 0
#     for i in range(n):
#         acc += int(a[i])
#         prefix_sum.append(acc)
#     result = 0
#     seen_left[0] = 1
#     for i in range(n):
#         right = prefix_sum[i] - i
#         seen_left[right-1] += 1
#         result += seen_left[right-1] - 1
#         print(seen_left)
        
#     print(result)












































