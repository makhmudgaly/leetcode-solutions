import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        
        heap = []
        heapq.heapify(heap)
        for i in range(n):
            for j in range(m):
                heapq.heappush(heap, matrix[i][j])
        
        for i in range(k-1):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)
        
        