class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n - 1

        while pivot >= 1 and nums[pivot] <= nums[pivot-1]:
            pivot -= 1
        
        if pivot != 0:
            right = n - 1
            while nums[right] <= nums[pivot - 1]:
                right -= 1
            
            nums[pivot-1], nums[right] = nums[right], nums[pivot-1]
        
        left = pivot
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



        