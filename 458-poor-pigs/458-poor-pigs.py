class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tries = minutesToTest / minutesToDie
        number = 0
        while ((tries + 1) ** number < buckets):
            number+=1
    
        return number;