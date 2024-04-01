class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drank = numBottles
        numBottles = 0
        while empty >= numExchange:
            numBottles += 1
            empty -= numExchange
            numExchange += 1
            drank += 1
            empty += 1
            
        return drank