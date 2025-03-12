class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        counter = 0
        p = 0
        n = 0
        for i in nums:
            if i < 0:
                n+=1
            elif i>0:
                p+=1
        return max(n,p)