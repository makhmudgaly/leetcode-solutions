class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0 for x in range(len(nums)+1)]
        for idx, num in enumerate(nums):
            self.arr[idx+1] = self.arr[idx] + num
            

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# 1, 2, 3, 4, 5
# 1, 3, 6, 10, 15

# 2, 5, 9