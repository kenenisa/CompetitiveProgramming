class Solution:
    def swap(self,arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        return arr
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        while(True):
            l = i*2+1
            r = i*2+2
            if n > max(r, l):
                if arr[i] >= max(arr[l], arr[r]):
                    break
                elif arr[l] > arr[r]:
                    arr = self.swap(arr, i, l)
                    i = l
                else:
                    arr = self.swap(arr, i, r)
                    i = r
            elif l < n:
                if arr[l] > arr[i]:
                    arr = self.swap(arr, i, l)
                    i = l
                else:
                    break
            elif r < n:
                if arr[r] > arr[i]:
                    arr = self.swap(arr, i, r)
                    i = r
                else:
                    break
            else:
                break
        return arr
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        si = (n-2)//2

        for j in range(si,-1,-1):
            arr = self.heapify(arr,n,j)
        return arr
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        arr = self.buildHeap(arr, n)

        for last in range(n-1, 0, -1):
            arr = self.swap(arr, 0, last)
            arr = self.heapify(arr, last,0)
        return arr