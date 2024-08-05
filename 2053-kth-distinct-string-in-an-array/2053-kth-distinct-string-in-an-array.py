from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)
        distinct = []
        for word in arr:
            d[word] += 1
        
        for elem, count in d.items():
            if count == 1:
                distinct.append(elem)
        
        return distinct[k-1] if len(distinct) >= k else ""
        