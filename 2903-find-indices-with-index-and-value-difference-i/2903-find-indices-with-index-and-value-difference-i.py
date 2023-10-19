class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                idxDiff = abs(i - j)
                valDiff = abs(num1 - num2)
                if idxDiff >= indexDifference and valDiff >= valueDifference:
                    return [i, j]
        
        return [-1, -1]