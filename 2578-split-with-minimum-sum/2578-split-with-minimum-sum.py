class Solution:
    def splitNum(self, num: int) -> int:
        arr = "".join(sorted(str(num)))
        first = ""
        second = ""
        for i in range(0, len(arr), 2):
            first += arr[i]
        for i in range(1, len(arr), 2):
            second += arr[i]
            
        return int(first) + int(second)
            
        