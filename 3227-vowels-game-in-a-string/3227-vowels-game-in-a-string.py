class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'u', 'o', 'i'}
        vowel_count = 0
        
        for ch in s:
            if ch in vowels:
                vowel_count += 1
        
        if vowel_count == 0:
            return False
        
        if vowel_count % 2 != 0:
            return True
        
        if vowel_count % 2 == 0 and vowel_count - vowel_count + 1 == 1:
            return True
        
        return False