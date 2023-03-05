class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = -1
        index = 1
        while time > 0:
            if index == n or index == 1:
                direction *= -1
                
            index += direction
            time -= 1
        
        return index
        