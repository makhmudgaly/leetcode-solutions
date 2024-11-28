class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        
        is_alice_winning = True
        decrement = 10
        while n >= 0:
            n -= decrement
            decrement -= 1
            is_alice_winning ^= True
        
        return is_alice_winning
            