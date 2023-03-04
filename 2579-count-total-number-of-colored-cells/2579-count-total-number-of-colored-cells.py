class Solution:
    def coloredCells(self, n: int) -> int:
        c = 2*n - 1
        ans = (c**2 / 2)
        return int(ans + .5)