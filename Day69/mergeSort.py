arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7, 55, 3, 5, 8, 6, 9, 1, 6, 7]

def mergeSort(a):
    n = len(a)
    if n < 2:
        return a
    left = mergeSort(a[:n//2])
    right = mergeSort(a[n//2:])

    # merge left and right
    merge = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    
    # the rest of the items
    for k in range(i, len(left)):
        merge.append(left[k])

    for k in range(j, len(right)):
        merge.append(right[k])

    return merge

m = mergeSort([100] * (10**8))
print(len(m))