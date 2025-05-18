class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.dfs(0, set(), set(), set(), n)
        return self.res

    def dfs(self, r, diagonal_set, anti_diagonal_set, cols_set, n):
        if r == n:
            self.res += 1
            return
        
        for c in range(n):
            if ( c in cols_set
                or (r+c) in anti_diagonal_set
                or (r-c) in diagonal_set
            ):
                continue
            
            cols_set.add(c)
            anti_diagonal_set.add(r+c)
            diagonal_set.add(r-c)

            self.dfs(r+1, diagonal_set, anti_diagonal_set, cols_set, n)

            cols_set.remove(c)
            anti_diagonal_set.remove(r+c)
            diagonal_set.remove(r-c)