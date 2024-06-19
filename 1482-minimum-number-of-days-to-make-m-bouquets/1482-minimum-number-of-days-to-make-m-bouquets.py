class Solution:
    def get_bouquets(self, bloomDay, target_day, k):
            bouquets = 0
            count = 0
            for day in bloomDay:
                if day <= target_day:
                    count += 1
                else:
                    count = 0
                
                if count == k:
                    bouquets += 1
                    count = 0
            
            return bouquets
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        min_day = 0
        max_day = max(bloomDay)
        ans = -1
        
        if m * k > len(bloomDay):
            return -1
        
        while min_day <= max_day:
            mid = (min_day + max_day) // 2
            
            if self.get_bouquets(bloomDay,mid,k) >= m:
                ans = mid
                max_day = mid - 1
            else:
                min_day = mid + 1
        
        return ans
        
                