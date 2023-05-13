class Solution:
    def countArrangement(self, n: int) -> int:
        self.result = 0

        def backtrack(i,arr):
            if i >= n + 1:
                self.result += 1
                return 
            for j in range(1,n+1):
                if j not in arr and (i % j == 0 or j % i == 0):
                    arr.append(j)
                    backtrack(i+1,arr)
                    arr.pop()
        backtrack(1,[])
        return self.result
        
        