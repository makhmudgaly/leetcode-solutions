class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = []
        for idx, num in enumerate(nums):
            right -= num
            ans.append(abs(left - right))
            left += num
        
        return ans