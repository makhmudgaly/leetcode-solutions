class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n = len(citations)
        right = n - 1
        
        
        while left <= right:
            mid = (left + right ) // 2
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                right -= 1
            else:
                left +=1
        
        return n - (right + 1)