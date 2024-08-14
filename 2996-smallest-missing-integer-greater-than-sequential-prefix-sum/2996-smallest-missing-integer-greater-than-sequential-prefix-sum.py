class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        max_prefix = prefix_sum
        right = 0
        d = Counter(nums)
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                break
                
            prefix_sum += nums[i]
        
        while True:
            if prefix_sum not in d:
                return prefix_sum
            prefix_sum +=1