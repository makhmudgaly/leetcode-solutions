class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        counter = 0
        
        while mainTank > 0:
            counter += 1
            ans += 1
            
            if counter == 5 and additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
                counter = 0
            
            mainTank -= 1
        
        return ans * 10