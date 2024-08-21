class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0]*(last_day+1)
        
        idx = 0
        for day in range(1, last_day+1):
            if day < days[idx]:
                dp[day] = dp[day-1]
            else:
                idx+=1
                _1day = dp[day-1] + costs[0]
                _7day = dp[max(0, day-7)] + costs[1]
                _30day = dp[max(0, day-30)] + costs[2]
                
                dp[day] = min(_1day,_7day,_30day)
        
        return dp[last_day]