class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity = sorted(capacity, reverse=True)
        print(capacity)
        cap = 0
        for idx, val in enumerate(capacity):
            cap += val
            if total_apples <= cap:
                return idx + 1
        
        return idx