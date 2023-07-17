class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        n = len(cost)
        
        if n < 3:
            return sum(cost)
        
        for i in range(n):
            if i % 3 != n % 3:
                ans += cost[i]
        return ans