class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        prev = 0
        count = 0
        for i in range(n):
            if i % 7 == 0:
                prev += 1
                count = prev
                money += prev
            else:
                count += 1
                money += count
        
        return money
            
            
        