from collections import defaultdict
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        d = defaultdict(list)
        ans = []
        for idx, num in enumerate(nums):
            d[num].append(idx)
            
        for q in queries:
            if not x in d:
                ans.append(-1)
            elif len(d[x]) < q:
                ans.append(-1)
            else:
                ans.append(d[x][q-1])
                
                
        return ans
        