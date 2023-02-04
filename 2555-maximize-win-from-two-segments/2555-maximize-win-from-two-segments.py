from collections import defaultdict
class Solution:
    def maximizeWin(self, prizes: List[int], k: int) -> int:
        N = len(prizes)
        best = [0] * (N + 1)

        ret = 0
        for i in range(N - 1, -1, -1):
            r = bisect.bisect_left(prizes, prizes[i] + k + 1)
            ret = max(ret, r - i + best[r])
            best[i] = max(r - i, best[i + 1])
        
        return ret