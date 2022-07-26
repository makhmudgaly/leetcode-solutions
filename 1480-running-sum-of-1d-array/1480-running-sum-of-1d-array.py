class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        ans = []
        for num in nums:
            sum += num
            ans.append(sum)
        return ans