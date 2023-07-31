class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for num in hours:
            if num >= target:
                ans += 1
        
        return ans