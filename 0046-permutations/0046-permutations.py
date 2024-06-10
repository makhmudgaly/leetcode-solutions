class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]] 
        for i in nums:
            n = nums.pop(0)
            subset = self.permute(nums)
            for i in subset:
                i.append(n)
            res.extend(subset)
            nums.append(n)
        return res
                    
                
        