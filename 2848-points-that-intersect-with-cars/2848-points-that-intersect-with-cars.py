class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr = [0] * 101
        for (start, end) in nums:
            for num in range(start, end+1):
                arr[num] += 1
        
        count = 0
        for i in arr:
            if i > 0:
                count += 1
        
        return count