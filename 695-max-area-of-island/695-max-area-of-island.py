class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = -1
        seen = set()
        
        def dfs(r,c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            
            seen.add((r,c))
            
            return (1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1))
        
        return max(dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])))
        
        
        