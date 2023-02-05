class Solution:
    def binaryGap(self, n: int) -> int:
        bin_str = bin(n)[2:]
        ans = 0
        pos = []
        for idx,bit in enumerate(bin_str):
            if bit == '1':
                pos.append(idx)
        
        for i in range(len(pos)-1):
            ans = max(abs(pos[i] - pos[i+1]), ans)
        
        return ans