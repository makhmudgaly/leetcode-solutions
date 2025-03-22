class Interval:
    def __init__(self, x,y):
        self.start = x
        self.end = y

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        B = Interval(*toBeRemoved)
        ans = []

        for interval in intervals:
            A = Interval(*interval)
            if A.start > B.end or A.end < B.start:
               ans.append(interval) 
                
            else:
                if A.start < B.start:
                    ans.append([A.start, B.start])
                
                if B.end < A.end:
                    ans.append([B.end, A.end])


        return ans