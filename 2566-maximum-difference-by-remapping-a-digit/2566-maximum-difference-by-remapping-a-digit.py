class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = num
        min_num = num
        
        for i in range(10):
            for j in range(10):
                if i != j:
                    new_num = int(str(num).replace(str(i), str(j)))
                    max_num = max(max_num, new_num)
                    min_num = min(min_num, new_num)
        
        return max_num - min_num
                    