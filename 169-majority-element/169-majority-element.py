class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums)/2
        dict = {}
        for num in nums:
            dict[num] = dict.get(num,0) + 1
            if dict[num] > target:
                return num
        