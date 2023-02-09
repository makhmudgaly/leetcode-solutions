class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        print(words)
        count = 0
        for word in words:
            valid = True
            seen = False
            for idx, letter in enumerate(word):
                
                if letter.isdigit() or (letter in '!.,' and idx != len(word) - 1):
                    valid = False
                    break
                
                if letter == '-':
                    if seen or idx == 0 or idx == len(word)-1 or not word[idx+1].isalpha():
                        valid = False
                        break
                    seen = True
            
            count += valid
                
        return count
                
        