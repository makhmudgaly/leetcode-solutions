class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [str(x) for x in range(1, n + 1)]
        return sorted(ans)