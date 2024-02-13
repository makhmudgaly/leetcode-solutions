class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        ans = []
        c = 0
        for idx in range(len(n)-1,-1,-1):
            if c == 3:
                ans.append(".")
                c = 0
                
            ans.append(n[idx])
            c += 1
            
            
        
        return "".join(ans[::-1])
                
                