class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            curr_max = -1
            prev = nums[i]
            for j in range(i+1,i+k):
                if prev != nums[j]-1:
                    ans.append(-1)
                    break
                prev = nums[j]
            else:
                ans.append(prev)
        
        return ans
                