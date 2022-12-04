class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        n = len(skill)
        
        desired = skill[0] + skill[-1]
        ans = 0
        for idx in range(n//2):
            if desired != skill[idx] + skill[n-idx-1]:
                return -1
            ans += skill[idx] * skill[n-idx-1]
            desired = skill[idx] + skill[n-idx-1]
        
        return ans
        