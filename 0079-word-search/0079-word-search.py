class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [(1,0),(-1,0), (0,1), (0,-1) ]
        
        def dfs(row, col, matched):
            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] != word[matched]:
                return False
            
            if matched == len(word) - 1:
                return True
            
            board[row][col] = "#"
            for (x,y) in dirs:
                if dfs(row+x, col+y, matched + 1):
                    return True
            board[row][col] = word[matched]
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
                    
        return False
        