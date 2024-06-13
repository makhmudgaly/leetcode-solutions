class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        
        ans = 0
        
        for idx, seat in enumerate(seats):
            ans += abs(seat - students[idx])
            
        return ans