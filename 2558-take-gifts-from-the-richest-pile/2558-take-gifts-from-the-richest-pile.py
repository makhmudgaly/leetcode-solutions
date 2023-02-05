class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for day in range(k):
            max_idx = 0
            max_val = 1
            for idx, val in enumerate(gifts):
                if val > max_val:
                    max_val = val
                    max_idx = idx
            
            gifts[max_idx] = int(gifts[max_idx] ** .5)
        
        return sum(gifts)