from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = deque()
        n = len(nums)
        k = k % n
        for i in range(n):
            new_idx = (i + k) % n
            stack.append((new_idx, nums[i]))
        
        while stack:
            new_idx, val = stack.pop()
            nums[new_idx] = val
        