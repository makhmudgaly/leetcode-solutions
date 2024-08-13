class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def backtrack(i, subset):
            if i == n:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)

            subset.pop()

            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])

        return res