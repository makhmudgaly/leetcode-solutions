class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def helper(word):
            d = {}
            return [d.setdefault(c, len(d)) for c in word]
        
        pattern = helper(pattern)
        
        return [word for word in words if helper(word) == pattern]
        

        