class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_flips = col_flips = 0
        
        # count flips to make rows palindromic
        
        for row in range(m):
            l,r = 0, n-1
            count = 0
            while l < r:
                if (grid[row][l] != grid[row][r]):
                    count += 1
                l+=1
                r-=1
            row_flips += count
        
        # count flips to make cols palindromic
        for col in range(n):
            l,r = 0, m-1
            count = 0
            while l < r:
                if (grid[l][col] != grid[r][col]):
                    count += 1
                l+=1
                r-=1
            col_flips += count
        
        return min(row_flips, col_flips)