class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        state = {chr(97+i):i+1 for i in range(0, 26)}
        
        for idx, val in enumerate(chars):
            letter_val = vals[idx]
            state[val] = letter_val
        
        arr_state = [state[ch] for ch in s]
        
        ans = 0
        cost = 0
        for val in arr_state:
            cost = max(0, cost + val)
            ans = max(ans, cost)
        
        return ans
        