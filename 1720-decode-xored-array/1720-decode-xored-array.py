class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i,num in enumerate(encoded):
            arr.append(arr[i] ^ num)
        return arr
        