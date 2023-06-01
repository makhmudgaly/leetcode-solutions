class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        
        for idx in range(0, len(nums), 2):
            freq = nums[idx]
            val = nums[idx+1]
            
            for cnt in range(freq):
                ans.append(val)
        
        return ans