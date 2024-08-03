class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)       

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        copy = list(self.array)
        for idx in range(len(self.array)):
            rand = random.randrange(len(copy))
            self.array[idx] = copy.pop(rand)
        
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()