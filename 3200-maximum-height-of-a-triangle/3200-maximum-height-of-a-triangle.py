class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        is_red_first = True
        red_height = 0
        blue_height = 0
        
        red_height = self.build_triangle(red, blue, True)
        blue_height = self.build_triangle(red, blue, False)
        return max(red_height, blue_height)
    
    def build_triangle(self, red,blue,is_red):
        level = 1
        height = 0
        while red >= 0 and blue >= 0:
            if is_red:
                red -= level
            else:
                blue -= level
            
            if red < 0 or blue < 0:
                break
            level += 1
            height += 1
            is_red = not is_red
        
        return height