class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c=0
        num = str(num)
        for i in range(len(num)-k+1):
            b = int(num[i:i+k])
            
            if b !=0 and int(num) % b == 0:
                c+=1
        return c
        