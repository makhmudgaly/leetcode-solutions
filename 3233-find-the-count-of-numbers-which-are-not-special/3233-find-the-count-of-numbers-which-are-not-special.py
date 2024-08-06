class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        limit = int(sqrt(r))
        
        primes = [True]*(limit+1)
        primes[0]=False
        primes[1]=False
        special = 0
        
        for i in range(2, int(math.sqrt(limit)) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False
        
        for i in range(len(primes)):
            if primes[i]:
                if l <= i*i <=r:
                    special += 1
        
        total = r - l + 1
        
        return total - special
                