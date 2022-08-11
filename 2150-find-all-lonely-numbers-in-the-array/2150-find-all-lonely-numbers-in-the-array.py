from collections import defaultdict
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        ans = []
        for num in nums:
            d[num]+=1
        
        for key in d:
            val = d[key]
            if val == 1 and int(key) - 1 not in d and int(key) + 1 not in d:
                ans.append(int(key))
        
        return ans
        