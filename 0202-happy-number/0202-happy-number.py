class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(n):
            digit_sum = 0
            while n > 0:
                digit = n % 10
                n //= 10
                digit_sum += digit ** 2
            
            return digit_sum
        slow = fast = n
        while True:
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))
            if fast == 1:
                return True
            
            if slow == fast:
                return False

        