class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        ans = []
        
        subset = []
        
        def backtrack(idx):
            if idx >= n:
                ans.append(subset.copy())
                return
            
            # go left on tree and include to subset
            subset.append(nums[idx])
            backtrack(idx+1)
            
            # go right on tree and exclude from subset
            subset.pop()
            backtrack(idx+1)
            
        backtrack(0)
        return ans
            
            
                
                
        