"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        results = []
        def binarySearch(x,start,end):
            if start == end: return start
            if end - start == 1:
                if customfunction.f(x,end) == z:
                    return end
                return start
            middle = (start+end)//2
            if customfunction.f(x,middle) == z:
                return middle
            elif customfunction.f(x,middle) > z:
                return binarySearch(x,start,middle-1)
            return binarySearch(x,middle+1,end)
        for x in range(1,z+1):
            if customfunction.f(x,1) > z:
                return results
            y = binarySearch(x,1,z)
            if customfunction.f(x,y) == z:
                results.append([x,y])
        return results
