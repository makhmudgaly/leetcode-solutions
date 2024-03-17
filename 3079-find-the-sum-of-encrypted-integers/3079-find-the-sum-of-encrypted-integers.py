class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            max_dig = int(max(list(str(num))))
            n = len(str(num))
            ans += int(f"1"*n) * max_dig
        
        return ans