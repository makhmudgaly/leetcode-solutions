class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        prev_el = word[0]
        count = 0
        for ch in word:
            if ch != prev_el:
                comp += f"{count}{prev_el}"
                count = 0
                prev_el = ch
            
            if count == 9:
                comp += f"{count}{prev_el}"
                count = 0
            count += 1
        comp += f"{count}{prev_el}"
        return comp