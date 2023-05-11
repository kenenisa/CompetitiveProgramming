class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        index = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                manhattan = abs(x - points[i][0]) + abs(y - points[i][1])
                if index == -1:
                    result = manhattan
                    index = i
                else:
                    if manhattan < result:
                        index = i
                        result = manhattan
                    
        return index