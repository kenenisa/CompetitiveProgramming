from collections import defaultdict 
class Solution: 
    def countPairs(self, deliciousness) -> int: 
        df=defaultdict(int) 
        result=0 
        for d in deliciousness: 
            for i in range(22): 
                result+=df[2**i-d] 
            df[d]+=1 
        return result%(10**9+7) 


if __name__=="__main__": 
    solution=Solution() 
    deliciousness = [1,3,5,7,9] 
    res =solution.countPairs(deliciousness) 
    print(res)