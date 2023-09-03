class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            num = str(num)
            if len(num) % 2 == 0:
                first = sum([int(x) for x in num[:len(num)//2]])
                second = sum([int(x) for x in num[len(num)//2:]])
                if first == second:
                    ans += 1
        return ans