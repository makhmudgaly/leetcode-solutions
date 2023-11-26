class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [idx for (idx, val) in enumerate(words) if x in val]