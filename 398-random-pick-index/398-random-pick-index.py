import random

class Solution:

    def __init__(self, nums: List[int]):
        self.dict = {}
        for idx, num in enumerate(nums):
            if num not in self.dict:
                self.dict[num] = []
            self.dict[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)