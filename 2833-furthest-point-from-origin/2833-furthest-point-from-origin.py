class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        all_l = abs(sum([-1 if x=='L' else 1 for x in list(moves.replace('_', 'L'))]))
        all_r = abs(sum([-1 if x=='L' else 1 for x in list(moves.replace('_', 'R'))]))
        
        if all_l >= all_r:
            return all_l
        return all_r
            