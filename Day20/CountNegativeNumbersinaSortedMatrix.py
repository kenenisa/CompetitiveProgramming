class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        def binarySearch(m,start,end):
            if start == end: return end
            if end - start == 1: 
                if m[start] < 0:
                    return start
                return end
            middle = int((start + end)/2)
            if m[middle] < 0:
                return binarySearch(m,start,middle)
            return binarySearch(m,middle,end)

        for m in grid:
            m_l = len(m)
            bs = 0
            if m[m_l - 1] >=0:continue
            if m[0] >= 0:
                bs = binarySearch(m,0,m_l-1)
            count += m_l - bs
        return count
