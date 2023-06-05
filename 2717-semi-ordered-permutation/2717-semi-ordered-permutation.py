class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        min_v = nums.index(1)
        max_v = nums.index(n)
        
        if min_v < max_v:
            return min_v + (n-max_v-1)
        
        return min_v + (n-max_v-1) - 1