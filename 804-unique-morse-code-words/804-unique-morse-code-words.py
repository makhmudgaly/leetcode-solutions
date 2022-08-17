class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        dict = {}
        
        for word in words:
            morse_version = ""
            for ch in word:
                letter_idx = ord(ch) - ord('a')
                morse_version += alpha[letter_idx]
            
            dict[morse_version] = word
        
        return len(dict.items())
                