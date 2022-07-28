class Solution:
    def sortSentence(self, s: str) -> str:
        s = [x[:-1] for x in sorted(s.split(' '), key=lambda x:int(x[-1]))]
        return " ".join(s)
        