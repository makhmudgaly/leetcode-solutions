class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols_map = defaultdict(int)
        rows_map = defaultdict(int)
        n = len(grid)
        ans = 0
        
        for row in range(n):
            row_hash = ""
            for col in range(n):
                row_hash += str(grid[row][col])+"#"
            rows_map[row_hash] += 1
            
        for col in range(n):
            col_hash = ""
            for row in range(n):
                col_hash += str(grid[row][col])+"#"
            
            cols_map[col_hash] += 1
            
        for row_hash in rows_map:
            if row_hash in cols_map:
                ans += cols_map[row_hash] * rows_map[row_hash]
        
        return ans
            
        