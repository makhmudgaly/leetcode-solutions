class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ""
        for ch in s.lower():
            if ch.isalnum():
                filtered_string += ch

        left, right = 0, len(filtered_string) - 1
        while left < right:
            if filtered_string[left] != filtered_string[right]:
                return False
            left += 1
            right -= 1
        
        return True
        