class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        d = {
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1),
            "UP": (-1, 0)
        }
        
        row = 0
        col = 0
        for command in commands:
            (x,y) = d.get(command)
            row = row + x
            col = col + y
        
        return row * n + col