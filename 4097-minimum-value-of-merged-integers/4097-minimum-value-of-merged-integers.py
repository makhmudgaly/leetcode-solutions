class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float("inf")
        for i in range(0, n, 2):
            f = get_multiple_score(nums[i])
            s = get_multiple_score(nums[i + 1])
            new_num = (nums[i] * (10 ** s)) + nums[i+1]
            ans = min(ans, new_num)
        
        return ans
    
def get_multiple_score(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
    
    return count