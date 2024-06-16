class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        for i in range(len(hours)):
            for j in range(i, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0 and i < j:
                    ans += 1
                    
        return ans