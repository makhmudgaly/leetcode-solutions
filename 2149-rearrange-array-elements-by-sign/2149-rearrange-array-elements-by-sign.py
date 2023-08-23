class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos_idx = 0
        neg_idx = 1
        for num in nums:
            if num > 0:
                ans[pos_idx] = num
                pos_idx += 2
            else:
                ans[neg_idx] = num
                neg_idx += 2
        
        return ans
        