class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minX, maxX = len(grid), -1
        minY, maxY = len(grid), -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    minX = min(minX, i)
                    maxX = max(maxX, i)
                    minY = min(minY, j)
                    maxY = max(maxY, j)
                  
        return (maxY - minY + 1) * (maxX - minX + 1)