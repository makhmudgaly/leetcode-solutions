class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        profit = 0
        for price in prices:
            
            min_price = min(price, min_price)
            if price - min_price > profit:
                profit = price - min_price
        
        return profit