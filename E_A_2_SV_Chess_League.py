n,k=list(map(int,input().split()))
a = list(map(int,input().split()))
idx = [i for i in range(2**n)]

def mergeSort(ic):
    n = len(ic)
    if n < 2:
        return ic
    left = mergeSort(ic[:n//2])
    right = mergeSort(ic[n//2:])

    # merge left and right
    merge = []
    for l in left:
        for r in right:
            if a[r] - a[l] <= k:
                merge.append(l)
                break
    for r in right:
        for l in left:
            if a[l] - a[r] <= k:
                merge.append(r)
                break


    return merge
print(*sorted(map(lambda item:item + 1,mergeSort(idx))))


# result = []
# def recur(ic):
#     n = len(ic)
#     if n == 0:
#         return
#     if n == 1:
#         result.append(ic[0])
#         return
#     first = []
#     second = []
#     third = []
#     fourth = []
#     flag = True
#     for i in range(0,n,2):
#         if abs(a[ic[i]] - a[ic[i+1]]) > k:
#             if a[ic[i]] > a[ic[i+1]]:
#                 first.append(ic[i])
#                 second.append(ic[i])
#                 third.append(ic[i])
#                 fourth.append(ic[i])
#             else:
#                 second.append(ic[i+1])
#                 first.append(ic[i+1])
#                 third.append(ic[i+1])
#                 fourth.append(ic[i+1])
 
#         else:
#             first.append(ic[i])
#             second.append(ic[i+1])
#             if flag:
#                 third.append(ic[i])
#                 fourth.append(ic[i+1])
#                 flag = False
#             else:
#                 third.append(ic[i+1])
#                 fourth.append(ic[i])
#                 flag = True
#     recur(first)
#     recur(second)
#     recur(third)
#     recur(fourth)
# recur(idx)
# print(*sorted(map(lambda item: item + 1 ,list(set(result)))))