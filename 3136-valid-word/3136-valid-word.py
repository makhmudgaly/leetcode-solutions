class Solution:
    def isValid(self, word: str) -> bool:
        state = [0]*2
        vowels = ('a', 'e', 'i', 'o', 'u')
        consonants = ('')
        if len(word) < 3:
            return False
        
        for ch in word:
            if not ch.isalnum():
                return False
            
            
            if ch.lower() in vowels and ch.isalpha():
                state[0] += 1
            if not ch.lower() in vowels and ch.isalpha():
                state[1] +=1
        
        return all(state)