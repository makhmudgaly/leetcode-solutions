class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def find_primes(num):
            div = 2
            prime_factors = set()
            while num > 1:
                while num % div == 0:
                    num /= div
                    prime_factors.add(div)
                div += 1
            return prime_factors
        
        ans = set()
        
        for num in nums:
            ans.update(find_primes(num))
            
        return len(ans)