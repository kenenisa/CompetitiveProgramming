class Solution: 
    def select(self, arr, i):
        # code here 
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                i = j
        return i
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            s = self.select(arr,i)
            arr[s],arr[i]= arr[i],arr[s]
        return arr