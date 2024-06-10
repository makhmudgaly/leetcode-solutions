class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def calculate_max_sum(arr, k, dp, start):
            n = len(arr)
            if start >= n:
                return 0
            
            if dp[start] != -1:
                return dp[start]
            
            currMax, ans = 0, 0
            end = min(n, start+k)
            for i in range(start, end):
                currMax = max(currMax, arr[i])
                ans = max(ans, currMax*(i-start+1) + calculate_max_sum(arr, k, dp, i + 1))
            
            dp[start] = ans
            return ans
        
        dp = [-1]*len(arr)
        return calculate_max_sum(arr, k, dp, 0)