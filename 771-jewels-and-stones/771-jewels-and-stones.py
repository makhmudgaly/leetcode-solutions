class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for jewel in jewels:
            count += stones.count(jewel)
        return count
        