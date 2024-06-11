class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos_in_arr_2 = {}
        n = len(arr2)
        
        for i in range(n):
            pos_in_arr_2[arr2[i]] = i
    
        
        return sorted(arr1, key=lambda x: pos_in_arr_2[x] if x in pos_in_arr_2 else n+x)
        