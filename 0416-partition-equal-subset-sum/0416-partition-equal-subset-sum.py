class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur}
                if target in cur:
                    return True
            
            return False

        
        