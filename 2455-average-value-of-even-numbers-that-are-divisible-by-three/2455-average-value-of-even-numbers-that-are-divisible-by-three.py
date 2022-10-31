class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        c = 0
        
        for num in nums:
            if num % 6 == 0:
                s+=num
                c+=1
        
        return 0 if c == 0 else s//c
        