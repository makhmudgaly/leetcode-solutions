class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        
        for idx, height in enumerate(heights):
            if height != expected[idx]:
                ans += 1
                
        return ans
        