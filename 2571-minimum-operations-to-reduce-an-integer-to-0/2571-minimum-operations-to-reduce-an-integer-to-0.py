import math

class Solution:
    def minOperations(self, n: int) -> int:
        return (n ^ (n * 3)).bit_count()