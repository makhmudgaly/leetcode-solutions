from collections import deque
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        
        queue = deque(range(1, n))
        prev = 0
        win_count = 0
        
        while True:
            curr = queue.popleft()
            
            if skills[prev] > skills[curr]:
                win_count += 1
                queue.append(curr)
            else:
                win_count = 1
                queue.append(prev)
                prev = curr
            
            if win_count == k or win_count >= n - 1:
                return prev
                