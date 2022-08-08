class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dict= {}
        for num in range(lo,hi+1):
            power = 0
            x = int(num)
            while(x != 1):
                if x % 2 == 0:
                    x /=2
                else:
                    x = 3*x + 1
                power+=1
            
            dict[num] = power
            
        ans = [x for x in range(lo,hi+1)]
        
        return sorted(ans, key=lambda x:dict[x])[k-1]