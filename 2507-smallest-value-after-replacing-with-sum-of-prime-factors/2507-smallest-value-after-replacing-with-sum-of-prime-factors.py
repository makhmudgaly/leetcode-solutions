class Solution:
    def smallestValue(self, n: int) -> int:
        def calculate_prime_factor_sum(num):
            div = 2
            local_sum = 0
            while num > 1:
                while num % div == 0:
                    num /= div
                    local_sum += div
                div += 1
            return local_sum
        
        sums = set()
        
        # If we see repeated prime_sum then it means end of cycle
        while n not in sums:
            prime_sum = calculate_prime_factor_sum(n)
            sums.add(n)
            n = prime_sum
        
        return n
        