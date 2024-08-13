class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = float("-inf")
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        m , n = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >=n or grid[row][col] == 0 or (row,col) in visited:
                return 0

            visited.add((row,col))
            area = 1
            for (x,y) in dirs:
                area += dfs(row + x, col + y)
            return area
        

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans
        
        
        