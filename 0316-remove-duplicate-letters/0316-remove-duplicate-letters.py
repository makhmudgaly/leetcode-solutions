from collections import deque
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freqs = [-1]*26
        
        # keep last occurrence
        for idx,ch in enumerate(s):
            freqs[ord(ch)-ord('a')] = idx
        
        stack = deque([])
        seen = set()
        
        for i, ch in enumerate(s):
            if ch in seen:
                continue
                
            while stack and ch < stack[-1] and i < freqs[ord(stack[-1])-ord('a')]:
                seen.remove(stack.pop())
            
            seen.add(ch)
            stack.append(ch)
        
        return "".join(stack)