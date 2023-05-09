class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pref_set = set()
        suff_set = set()
        
        pref = []
        suff = [0]
        ans = []
        
        for i in range(len(nums)):
            pref_set.add(nums[i])
            pref.append(len(pref_set))
            
        for i in range(len(nums)-1,-1,-1):
            suff_set.add(nums[i])
            suff.append(len(suff_set))
          
        suff = suff[::-1]
            
        for i in range(len(nums)):
            ans.append(pref[i] - suff[i+1])
            
        return ans