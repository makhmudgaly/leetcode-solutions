from collections import Counter

class Solution:
    def isFascinating(self, n: int) -> bool:
        new_str = str(n)
        new_str += str(2*n) + str(3*n)
        
        counter = Counter(new_str)
        
        if '0' in counter:
            return False
        
        for dig in range(1, 10):
            if counter[str(dig)] != 1:
                return False
            
        return True