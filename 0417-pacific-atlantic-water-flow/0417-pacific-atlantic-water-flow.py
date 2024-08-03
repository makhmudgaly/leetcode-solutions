class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        pacific = set()
        atlantic = set()
        
        
        def dfs(seen, heights, height ,i, j):
            m = len(heights)
            n = len(heights[0])
            if i<0 or j<0 or (i,j) in seen or i>=m or j>=n or heights[i][j] < height:
                return

            seen.add((i,j))
            for (x,y) in dirs:
                dfs(seen, heights, heights[i][j] ,i+x,j+y)
                
        for i in range(m):
            dfs(pacific, heights, float("-inf"), i, 0)
            dfs(atlantic, heights, float("-inf"), i, n-1)
            
        for j in range(n):
            dfs(pacific, heights, float("-inf"), 0, j)
            dfs(atlantic, heights, float("-inf"), m-1, j)
        
        return list(pacific.intersection(atlantic))
            
    