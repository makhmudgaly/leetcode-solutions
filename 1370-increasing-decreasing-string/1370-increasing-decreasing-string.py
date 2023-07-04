from collections import defaultdict
class Solution:
    def sortString(self, s: str) -> str:
        d = defaultdict(int)
        new_s = ""
        for ch in s:
            d[ch] += 1
        while sum(d.values()) > 0:
            for i in range(0,27):
                if d[chr(i+97)] > 0:
                    d[chr(i+97)]-=1
                    new_s += chr(i+97)

            for i in range(26,-1,-1):
                if d[chr(i+97)] > 0:
                    d[chr(i+97)]-=1
                    new_s += chr(i+97)
                
        return new_s