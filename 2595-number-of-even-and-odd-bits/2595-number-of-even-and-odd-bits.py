class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s = bin(n)[2:]
        odd = 0
        even = 0
        for idx, bit in enumerate(s[::-1]):
            if idx % 2 == 0 and bit == '1':
                even +=1 
            elif idx % 2 != 0 and bit == '1':
                odd += 1
        
        return [even, odd]