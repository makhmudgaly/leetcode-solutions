class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict = {}
        for idx, ch in enumerate(order):
            dict[ch] = idx
            
        s= sorted(s, key=lambda x: dict.get(x,0))
        
        return "".join(s)
        