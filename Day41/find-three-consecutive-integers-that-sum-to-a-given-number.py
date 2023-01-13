class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3:
            return [] 
        ni = (num - 3)//3 
        return [ni,ni+1,ni+2]