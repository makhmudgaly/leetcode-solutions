class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                # Check cell below
                if 0 <= i + 1 < m:
                    if grid[i][j] != grid[i+1][j]:
                        return False
                
                # Check cell on right
                if 0 <= j + 1 < n:
                    if grid[i][j] == grid[i][j+1]:
                        return False
        
        return True
            
            