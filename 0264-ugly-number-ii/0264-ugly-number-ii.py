class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        ans = [1] * n
        
        ptr_2, ptr_3, ptr_5 = 0, 0, 0
        
        for idx in range(1, n):
            next_2 = ans[ptr_2] * 2
            next_3 = ans[ptr_3] * 3
            next_5 = ans[ptr_5] * 5
            ans[idx] = min(next_2, next_3, next_5)
            
            if next_2 == ans[idx]: ptr_2 +=1 
            if next_3 == ans[idx]: ptr_3 +=1
            if next_5 == ans[idx]: ptr_5 +=1
        
        return ans[n-1]
                