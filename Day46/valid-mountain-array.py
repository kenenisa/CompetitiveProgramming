class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False
        inc = False
        dec = False
        for i in range(n-1):   
            if arr[i] == arr[i+1]:
                return False
            elif not inc and arr[i] < arr[i+1]:
                inc = True
            elif not inc and arr[i] > arr[i+1]:
                return False
            elif inc and arr[i] > arr[i+1]:
                dec = True
            elif dec and arr[i] < arr[i+1]:
                return False
        return inc and dec