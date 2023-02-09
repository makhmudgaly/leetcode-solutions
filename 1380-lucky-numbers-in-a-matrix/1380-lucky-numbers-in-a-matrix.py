class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        track = set()
        ans = []
        
        for i in range(m):
            row_min = mat[i][0]
            for j in range(n):
                row_min = min(row_min, mat[i][j])
            
            track.add(row_min)
            
        for j in range(n):
            col_max = mat[0][j]
            for i in range(m):
                col_max = max(col_max, mat[i][j])
            
            if col_max in track:
                ans.append(col_max)
                
        return ans
            
        