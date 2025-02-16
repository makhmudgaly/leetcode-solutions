class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for idx, num in enumerate(nums):
            left = idx - k if 0 <= idx - k < n else - 1
            right = idx + k if 0 <= idx + k < n else - 1
            if left > -1 and right > -1:
                total += num if num > nums[left] and num > nums[right] else 0
            elif left > - 1 and right == -1:
                total += num if num > nums[left] else 0 
            elif left == - 1 and right > -1:
                total += num if num > nums[right] else 0

        
        return total