class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) >> 1
            if eat_time(piles, mid) > h:
                left = mid + 1
            else:
                right = mid
        
        return left
        
    
def eat_time(piles, k):
    time = 0
    for pile in piles:
        time += pile // k
        time += 0 if pile % k == 0 else 1
    
    return time