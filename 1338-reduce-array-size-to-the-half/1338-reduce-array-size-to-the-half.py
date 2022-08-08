class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total = len(arr)
        half = total // 2
        dict = {}
        
        for num in arr:
            dict[num] = dict.get(num, 0) + 1
        
        values = sorted(list(dict.values()))
        idx = len(values) -1 
        c = 0
        while total > half:
            total -= values[idx]
            idx -=1
            c+=1
        
        return c