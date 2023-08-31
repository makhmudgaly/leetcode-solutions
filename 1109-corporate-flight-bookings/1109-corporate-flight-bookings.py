from collections import defaultdict
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for x in range(n+1)]
        for (first, last, seats) in bookings:
            ans[first-1] += seats
            ans[last] -= seats
        
        for idx in range(1, len(ans)):
            ans[idx] += ans[idx-1]
                
        return ans[:n]