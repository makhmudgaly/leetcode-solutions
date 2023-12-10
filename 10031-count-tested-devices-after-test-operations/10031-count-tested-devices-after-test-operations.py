class Solution:
    def countTestedDevices(self, b: List[int]) -> int:
        ans = 0
        for i, val in enumerate(b):
            if val == 0:
                continue
            
            for j in range(i + 1, len(b)):
                b[j] = max(0, b[j] - 1)
            ans += 1
        
        return ans