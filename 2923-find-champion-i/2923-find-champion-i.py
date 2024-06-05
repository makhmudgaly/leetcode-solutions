class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if all(grid[i][j] == 1 for j in range(len(grid)) if i!=j):
                return i