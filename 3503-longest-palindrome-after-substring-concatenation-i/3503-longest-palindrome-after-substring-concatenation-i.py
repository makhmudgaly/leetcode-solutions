class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        max_length = 0

        def find_longest_palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - left - 1

        for i in range(m+1):
            for j in range(n+1):
                combined_string = s[:i] + t[j:]
                
                for middle in range(len(combined_string)):
                    odd_length = find_longest_palindrome(combined_string, middle, middle)
                    even_length = find_longest_palindrome(combined_string, middle, middle + 1)

                    max_length = max(max_length, odd_length, even_length)
        
        return max_length
