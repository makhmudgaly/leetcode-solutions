class Solution:
    def findPeaks(self, m: List[int]) -> List[int]:        
        return [i for i in range(1, len(m)-1) if m[i-1] < m[i] > m[i+1]]