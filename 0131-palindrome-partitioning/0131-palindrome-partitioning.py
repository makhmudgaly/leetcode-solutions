class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrom(s,i,j):
                    partition.append(s[i: j+1])
                    dfs(j+1)
                    partition.pop()

        dfs(0)
        return res

    
    def isPalindrom(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        