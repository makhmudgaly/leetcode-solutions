class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(x for x in nums if x > 0)
        return len(s)
        