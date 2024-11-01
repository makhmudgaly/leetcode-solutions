class Solution:
    def makeFancyString(self, s: str) -> str:
        first, *rest = s
        queue = [first]
        count = 1
        for ch in rest:
            if queue[-1] == ch:
                count += 1
            else:
                count = 1
            
            if count < 3:
                queue.append(ch)
                
        
        return ''.join(queue)
            