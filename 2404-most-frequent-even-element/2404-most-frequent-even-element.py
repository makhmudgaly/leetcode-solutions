from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max_value = 0
        min_key = 1000000
        for num in nums:
            if num % 2 == 0:
                d[num]+=1
                max_value = max(max_value, d[num])
                
        for key,value in d.items():
            if value == max_value:
                min_key = min(min_key, key)
            
        return -1 if max_value == 0 else min_key
            
        
        