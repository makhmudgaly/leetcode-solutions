class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_arr = [[0]*len(img[0]) for _ in img]
        
        def smoother(x,y, img):
            curr_sum = 0
            curr_count = 0
            for new_row in (x-1, x, x+1):
                for new_col in (y-1, y, y+1):
                    if 0 <= new_row < len(img) and 0 <= new_col < len(img[0]):
                        curr_sum += img[new_row][new_col]
                        curr_count += 1
            
            
            return curr_sum//curr_count
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                new_arr[i][j] = smoother(i,j,img)
                
        return new_arr
                        