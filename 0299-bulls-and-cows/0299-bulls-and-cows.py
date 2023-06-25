from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        d = defaultdict(int)
        for idx in range(len(secret)):
            if secret[idx] == guess[idx]:
                bulls += 1
            else:
                if d[secret[idx]] > 0: cows+=1
                if d[guess[idx]] < 0: cows+=1
                    
                d[guess[idx]] += 1
                d[secret[idx]] -= 1
                
        
        return f"{bulls}A{cows}B"