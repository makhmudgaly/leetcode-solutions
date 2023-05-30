class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        bound = 0
        for idx, digit in enumerate(num):
            if digit != '0':
                bound = idx
        
        return num[:bound+1]