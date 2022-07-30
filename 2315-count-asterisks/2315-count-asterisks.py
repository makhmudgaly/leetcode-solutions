class Solution:
    def countAsterisks(self, s: str) -> int:
        arr = s.split('|')
        count = 0
        for i in range(0, len(arr), 2):
            count += arr[i].count('*')
        
        return count
        