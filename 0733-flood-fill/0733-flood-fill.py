class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def walk(i,j,src,to):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != src:
                return
            
            image[i][j] = to
            dirs = [(-1,0), (1,0), (0,1), (0,-1)]
            
            for (x,y) in dirs:
                walk(i+x,j+y,src,to)
        
        src = image[sr][sc]
        if src == color:
            return image
        walk(sr,sc,src,color)
        
        return image