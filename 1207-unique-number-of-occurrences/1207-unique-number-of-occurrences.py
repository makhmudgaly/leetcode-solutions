from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = defaultdict(int)
        
        for idx, num in enumerate(arr):
            dictionary[num] += 1
        
        return len(set(dictionary.values())) == len(dictionary.values())