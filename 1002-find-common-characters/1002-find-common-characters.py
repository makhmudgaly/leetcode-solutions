class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for letter in set(words[0]):
            min_count = float("inf")
            for word in words:
                min_count = min(min_count, word.count(letter))
                
            ans.extend([letter] * min_count)
        
        return ans
                