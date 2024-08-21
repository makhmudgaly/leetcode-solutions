
import math
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        
        
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a
        
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if gcd(i,j) == 1:
                    ans.append(f"{i}/{j}")
        return ans