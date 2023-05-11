class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key = lambda x: (x[1], x[1] - x[0]))
        shot_pointer = -float('inf')
        arrow = 0

        for baloon in sorted_points:
            if baloon[0] > shot_pointer:
                shot_pointer = baloon[1]
                arrow += 1
                
        return arrow
                
