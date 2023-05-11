class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        result = []

        def backtrack(i,mem):
            if i >= 3 and result[-1] != result[-2] + result[-3]: 
                return False

            if mem == '': 
                if i >= 3:
                    return True
                return False 

            for j in range(1, len(mem) + 1):
                cur = mem[:j]
                rest = mem[j:]

                if len(cur) > 1 and cur[0] == '0': 
                    break

                result.append(int(cur))
                l = backtrack(i + 1,rest)
                if l: 
                    return True
                result.pop()
            return False
        return backtrack(0,num)

        