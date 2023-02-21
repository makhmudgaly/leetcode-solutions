class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_level = 0
        for level in bank:
            ones = level.count("1")
            if ones == 0:
                continue
            
            # Edges between lasers = prev_level * current_num
            ans += prev_level*ones
            prev_level = ones
        
        return ans
        