class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for b in bills:
            if b == 5: five += 1
            elif b == 10: 
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if five == 0: 
                    return 0
                elif ten == 0:
                    if five < 3: 
                        return False
                    five -= 3
                else: 
                    five -= 1
                    ten -= 1 
        return True
                

        
