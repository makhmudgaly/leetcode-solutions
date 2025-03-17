class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        lower = lower_bound(nums, target)
        upper = upper_bound(nums, target)

        return [lower, upper]

def upper_bound(nums, target):
    left, right = 0 , len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid
    
    if nums[right] != target:
        return -1
    return right

def lower_bound(nums, target):
    left, right = 0 , len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
        
    if nums[left] != target:
        return -1
    
    return left
    