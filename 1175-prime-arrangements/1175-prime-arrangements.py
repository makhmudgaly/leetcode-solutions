import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        count = 1                                                     # number of primes, first prime is 2.
        for i in range(3, n + 1, 2):                                # only odd number could be a prime, if i > 2.
            factor = 3
            while factor * factor <= i:
                if i % factor == 0:
                    break 
                factor += 2    
            else:
                count += 1        
        
        # return ( math.factorial(count) * math.factorial(n-count)) %(10**9+7)
        return  math.factorial(count) * math.factorial(n - count) % (10**9 + 7)
        