class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'u', 'o', 'i'}
        
        for ch in s:
            if ch in vowels:
                return True
        
        return False