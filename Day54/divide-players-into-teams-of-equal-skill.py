class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0 
        right = len(skill)-1
        
        level = skill[0] + skill[-1]
        result = 0

        while(right > left):
            if(skill[right] + skill[left] == level):
                result = result + (skill[right] * skill[left])
            else:
                return -1
            right -= 1
            left += 1

        return result