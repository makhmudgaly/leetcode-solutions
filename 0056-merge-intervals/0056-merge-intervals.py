class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            B = intervals[i]
            A = merged[-1]

            if A[1] < B[0]:
                merged.append(B)
            else:
                merged[-1] = [A[0], max(A[1], B[1])]
        
        return merged