class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = 0
        for val in chalk:
            total += val
            if total > k:
                break
        
        k = k % total
        for idx, val in enumerate(chalk):
            if k < val:
                return idx
            
            k -= val
        
        return 0
            