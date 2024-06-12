class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def required_days(weights, cap):
            curr_weight, days = 0 , 1
            for w in weights:   
                if curr_weight + w > cap:
                    days += 1
                    curr_weight = w
                else:
                    curr_weight += w
            
            return days
        
        min_cap = max(weights)
        max_cap = sum(weights)
     
        while min_cap <= max_cap:
            mid = min_cap + (max_cap - min_cap) // 2
            if required_days(weights, mid) <= days:
                max_cap = mid - 1
            else:
                min_cap = mid + 1
        
        return min_cap
            