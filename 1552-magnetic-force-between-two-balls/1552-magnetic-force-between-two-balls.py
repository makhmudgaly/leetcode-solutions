class Solution:
    def can_place_balls(self, gap, position, m):
        prev_pos = position[0]
        ball_placed = 1
        
        for i in range(1, len(position)):
            curr_pos = position[i]
            if curr_pos - prev_pos >= gap:
                ball_placed += 1
                prev_pos = curr_pos
            
            if ball_placed == m:
                return True
        
        return False
    
    def maxDistance(self, position: List[int], m: int) -> int:
        ans = 0
        n = len(position)
        position.sort()
        low = 1
        high = (position[-1] // (m-1)) + 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.can_place_balls(mid, position, m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans