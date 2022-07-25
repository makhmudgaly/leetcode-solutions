class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        return str_num == str_num[::-1]
        