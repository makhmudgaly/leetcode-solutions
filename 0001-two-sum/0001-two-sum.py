class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx,num in enumerate(nums):
            if target-num in visited:
                return [idx, visited[target-num]]
            visited[num] = idx