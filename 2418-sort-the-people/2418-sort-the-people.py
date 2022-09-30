class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        for idx in range(len(names)):
            arr.append([names[idx], heights[idx]])
        
        arr = [el[0] for i, el in enumerate(sorted(arr, key=lambda x:x[1], reverse=True))]
        return arr
        