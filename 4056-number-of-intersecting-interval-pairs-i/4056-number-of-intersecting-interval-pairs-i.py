class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans += intersect(intervals[i], intervals[j])
        
        return ans

def intersect(a , b):
    return within(a,b) or within(b,a)

def within(a,b):
    return b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]
