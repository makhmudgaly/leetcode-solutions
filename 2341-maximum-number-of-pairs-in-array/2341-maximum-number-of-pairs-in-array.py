from collections import defaultdict
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
            
        leftover = 0
        pairs = 0
        
        for num in freq:
            leftover += freq[num] % 2
            pairs += freq[num] // 2
        
        return [pairs, leftover]