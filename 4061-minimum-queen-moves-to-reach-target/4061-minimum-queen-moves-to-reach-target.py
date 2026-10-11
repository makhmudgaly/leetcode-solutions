class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if target[0] == source[0] and target[1] == source[1]:
            return 0

        if source[0] == target[0] or source[1] == target[1]:
            return 1
        
        if (abs(target[0] - source[0]) == abs(target[1] - source[1])):
            return 1
        
        return 2
