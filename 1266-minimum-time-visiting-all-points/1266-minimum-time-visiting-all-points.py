class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        
        for i in range(1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[i-1]
            res += max(abs(x1-x2), abs(y1-y2))

        return res
