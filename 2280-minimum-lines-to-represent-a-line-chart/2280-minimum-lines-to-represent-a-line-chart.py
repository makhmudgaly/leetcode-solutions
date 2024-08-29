class Solution:
    def minimumLines(self, arr: List[List[int]]) -> int:
        if len(arr) == 1:
            return 0
            
        
        ans = 1
        arr.sort(key=lambda x: x[0])
        for i in range(2, len(arr)):
            p1, p2, p3 = arr[i], arr[i-1], arr[i-2]
            slope_prev = (p3[1] - p2[1]) * (p2[0] - p1[0])
            slope_curr = (p2[1] - p1[1]) * (p3[0] - p2[0])
            
            if slope_prev != slope_curr:
                ans += 1
            
        return ans