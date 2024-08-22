class Solution:
    def findComplement(self, num: int) -> int:
        level = 0
        ans = 0
        while num > 0:
            rem = num % 2
            num = num // 2
            
            ans += (1 if rem == 0 else 0)*(2**level)
            level += 1
        
        return ans