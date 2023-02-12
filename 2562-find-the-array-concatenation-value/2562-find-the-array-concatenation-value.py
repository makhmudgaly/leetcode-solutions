class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            ans += int(concat(nums[left], nums[right]))
            left += 1
            right -= 1
        
        if left == right:
            ans += nums[left]
        
        return ans
    
def concat(a, b):
    a = str(a)
    b = str(b)
    
    return a + b
    