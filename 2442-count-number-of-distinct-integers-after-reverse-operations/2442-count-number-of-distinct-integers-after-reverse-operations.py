class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()
        
        for num in nums:
            s.add(num)
            s.add(int(str(num)[::-1]))
        
        return len(s)