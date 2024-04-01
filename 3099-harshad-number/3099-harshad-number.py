class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits_sum = sum(int(digit) for digit in str(x))
        return digits_sum if x % digits_sum == 0 else -1