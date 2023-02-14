from collections import defaultdict
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bits = len(nums[0])
        d = defaultdict(int)
        
        for num in nums:
            integer = int(num,2)
            d[integer] = 1
        
        max_num = (2 ** bits) - 1
        
        while max_num != 0:
            if max_num not in d:
                res = bin(max_num)[2:]
                return "0"*(bits - len(res)) + res
            max_num -= 1
            
        return "0"
            
            
            