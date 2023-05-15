class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        arr = [0]*n
        ans = []
        arr[0] = 1
        next_idx = 0
        for i in range(1,n+1):
            next_idx = (i*k + next_idx)%n
            arr[next_idx] += 1
            if arr[next_idx] == 2:
                break
        
        for idx, val in enumerate(arr):
            if val == 0:
                ans.append(idx+1)
        
        return ans
        