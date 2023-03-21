class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                j = i + 1
            ans += i - j + 1

        return ans