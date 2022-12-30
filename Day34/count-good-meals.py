class Solution: 
    def countPairs(self, deliciousness) -> int: 
        df={}
        result=0 
        for d in deliciousness: 
            for i in range(22): 
                result+=df.get(2**i-d,0) 
            if df.get(d):
                df[d]+=1 
            else:
                df[d]=1
        return result%(10**9+7) 