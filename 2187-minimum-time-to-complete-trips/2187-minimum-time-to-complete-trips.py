class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips
        
        while left < right:
            mid = (left + right) // 2
            trips = 0
            for t in time:
                trips += mid // t
            
            if trips >= totalTrips:
                right = mid
            else:
                left = mid + 1
                
        return left