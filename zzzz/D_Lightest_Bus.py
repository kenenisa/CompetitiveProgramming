
# import sys, threading

# input = lambda: sys.stdin.readline().strip()

# def main():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         a = list(map(int,input().split()))
#         prefix = [0]
#         for aa in a:
#             prefix.append(aa + prefix[-1])
#         def recur(start,end):
#             global mi
#             if start >= n:
#                 return float('inf')
#             end = min(end,n)
#             return min(recur(end,end+18),recur(end,end+12),prefix[end] - prefix[start])
#         print(min(recur(0,12),recur(0,18)))

# if __name__ == '__main__':
    
#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    prefix = [0]
    for aa in a:
        prefix.append(aa + prefix[-1])

    result = min(prefix[min(n,12)],prefix[min(n,18)])

    for i in range(12,n,6):
        result = min(result,prefix[min(n,i+18)] - prefix[i], prefix[min(n,i+12)] - prefix[i])
    print(result)