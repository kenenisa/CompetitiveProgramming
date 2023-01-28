class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def getMaxWithIndex(ary):
            m = [0]
            for i in range(len(ary)):
                if(ary[i] > m[0]):
                    m = [ary[i],i]
            return m[1]
        n = len(arr)
        k = []
        for i in range(n):
            max_index = getMaxWithIndex(arr[:n]) + 1
            if(max_index < n):
                arr[:max_index] = reversed(arr[:max_index])
                k.append(max_index)
                arr[:n] = reversed(arr[:n])
                k.append(n)
            n -= 1
        return k