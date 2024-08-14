class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = [0,0]
        
        for h, w in dimensions:
            d = sqrt(h*h + w*w)
            a = h * w
            if d > ans[0]:
                ans = [d, a]
            elif d == ans[0]:
                ans = [d, max(a, ans[1])]
        return ans[1]