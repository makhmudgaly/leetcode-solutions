class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        def backtrack(curr, start, k):
            if k == 0:
                combs.append(curr.copy())
                return
            
            for i in range(start,n+1):
                curr.append(i)
                backtrack(curr, i+1, k-1)
                curr.pop()
        
        
        backtrack([], 1, k)
        return combs
        
        
        
        