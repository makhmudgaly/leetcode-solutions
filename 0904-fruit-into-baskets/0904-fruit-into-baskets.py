from collections import defaultdict

from itertools import islice
class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        bucket = defaultdict(int)
        left = 0
        ans = 0
        for right, fruit in enumerate(arr):
            bucket[fruit] += 1
            
            while len(bucket) > 2:
                bucket[arr[left]] -= 1
                if bucket[arr[left]] == 0:
                    del bucket[arr[left]]
                
                left += 1
            
            
            ans = max(ans, right - left + 1)
        
        return ans
        
        