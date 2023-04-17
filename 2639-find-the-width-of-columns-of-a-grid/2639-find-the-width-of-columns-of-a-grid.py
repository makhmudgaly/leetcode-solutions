class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(grid[0])):
            col_max = len(str(grid[0][i]))
            for j in range(len(grid)):
                col_max = max(col_max, len(str(grid[j][i])))
            
            ans.append(col_max)
            
        return ans