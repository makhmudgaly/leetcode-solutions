class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(grid, i, j, m, n):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            for (x,y) in dirs:
                dfs(grid, i+x, j+y, m, n)
                
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i*j == 0 or i == m-1 or j == n-1:
                    dfs(grid,i,j,m,n)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        
        return count
            