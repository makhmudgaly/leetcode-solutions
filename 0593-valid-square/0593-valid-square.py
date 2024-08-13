class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        
        def distance(p1, p2):
            return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        
        distances = [
            distance(p1, p2),
            distance(p1,p3),
            distance(p1,p4),
            distance(p2, p3),
            distance(p2, p4),
            distance(p3, p4)
        ]
        
        distances.sort()
        
        sides_equal = True
        prev = distances[0]
        for i in range(1,4):
            if prev != distances[i]:
                sides_equal = False
            prev = distances[i]
        
        return sides_equal and distances[4] == distances[5]