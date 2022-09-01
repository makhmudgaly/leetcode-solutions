class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = []
        for q in queries:
            s = 0
            c = 0
            for num in nums:
                if num > q or s+num > q:
                    break
                s+=num
                c+=1
            ans.append(c)
            
        return ans
                