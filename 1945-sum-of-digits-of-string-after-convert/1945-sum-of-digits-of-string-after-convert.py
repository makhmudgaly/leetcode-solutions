class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = "".join([str(ord(ch)-ord('a')+1) for ch in s])
       
        while k > 0:
            digit_sum = str(sum(int(digit) for digit in num))
            num = digit_sum
            k-=1
        
        return int(num)