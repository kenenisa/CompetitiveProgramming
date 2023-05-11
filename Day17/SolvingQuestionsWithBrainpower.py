class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        points = [0] * n
        points[-1] = questions[-1][0]

        for i in range(n-2,-1,-1):
            nxt = i + questions[i][1] + 1
            points[i] = max(questions[i][0], points[i + 1]) if nxt >= n else max(points[i+1],questions[i][0] + points[nxt])

        return points[0]
        # points = []
        # n = len(questions)
        # for i in range(n):
        #     p = []
        #     nxt = i + questions[i][1] + 1
        #     if nxt < n:
        #         for j in range(nxt,n):
        #             x = j
        #             point = questions[i][0]
        #             while x < n:
        #                 point += questions[x][0]
        #                 x += questions[x][1] + 1
        #             p.append(point)
        #         points.append(max(p))
        #     else:
        #         points.append(questions[i][0])
        # return max(points)