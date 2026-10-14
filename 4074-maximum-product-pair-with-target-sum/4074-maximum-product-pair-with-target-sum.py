class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        ans = (float('-inf'), [-1, -1])

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target and nums[i] > nums[j]):
                    if (nums[i] * nums[j] > ans[0]):
                        ans = (nums[i] * nums[j], [i, j])
        
        return ans[1]
        
