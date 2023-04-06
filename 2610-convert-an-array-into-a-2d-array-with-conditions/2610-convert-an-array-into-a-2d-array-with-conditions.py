from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        state = defaultdict(int)
        most_freq = 0
        for num in nums:
            state[num] += 1
            most_freq = max(state[num], most_freq)
            
        ans = [[] for x in range(most_freq)]
        
        for k, val in state.items():
            
            for i in range(val):
                ans[i].append(int(k))
        return ans