class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        t = ""
        for word in words:
            t += word[0]
        
        return t == s