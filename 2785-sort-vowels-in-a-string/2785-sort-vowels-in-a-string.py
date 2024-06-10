class Solution:
    def sortVowels(self, s: str) -> str:
        accepted_vowels = {'a', 'e', 'i', 'o', 'u'}
        vowels = [ch for ch in s if ch.lower() in accepted_vowels]
        vowels.sort(key=lambda x: ord(x))
        idx = 0
        s = list(s)
        for i in range(len(s)):
            if s[i].lower() in accepted_vowels:
                s[i] = vowels[idx]
                idx += 1
        
        return "".join(s)
        
            
        