from collections import Counter
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        counter = Counter(sorted(nums))
        hasNoValues = True
        while hasNoValues:
            stillHasValue = False
            for key, val in counter.items():
                stillHasValue |= val > 0

                if val > 0:
                    ans.append(key)
                    counter[key] -= 1
            hasNoValues = stillHasValue
        
        return ans

