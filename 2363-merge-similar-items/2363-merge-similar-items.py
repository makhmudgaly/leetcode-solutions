from collections import defaultdict
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict = defaultdict(int)
        ans = []
        
        for val, weight in items1 + items2:
            dict[val] += weight
          
        for key in sorted(dict.keys()):
            ans.append([key, dict[key]])
            
        return ans