class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.map = {}
        for i in range(self.n):
            for j in range(self.n):
                self.map[grid[i][j]] = [i,j]

    def adjacentSum(self, value: int) -> int:
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        i, j = self.map[value]
        return self.getNeighborsSum(i,j, dirs)
            

    def diagonalSum(self, value: int) -> int:
        dirs = [(1,-1), (1,1), (-1,1), (-1,-1)]
        i, j = self.map[value]
        return self.getNeighborsSum(i,j, dirs)

    def getNeighborsSum(self, i, j, dirs):
        total = 0
        for (x,y) in dirs:
            if i + x < 0 or j +y < 0 or i + x >= self.n or j + y >= self.n:
                continue
            total += self.grid[i+x][j+y]
        return total
# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)