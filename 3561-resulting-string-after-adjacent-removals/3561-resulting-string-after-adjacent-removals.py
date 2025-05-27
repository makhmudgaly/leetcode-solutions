class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        for ch in s:
            if len(stack) > 0 and is_adjacent(ch, stack[-1]):
                stack.pop()
            else:
                stack.append(ch) 

        return "".join(stack)


def is_adjacent(char_a, char_b):
    code_a = ord(char_a)
    code_b = ord(char_b)

    if abs(code_b - code_a) == 1:
        return True
    if abs(code_b - code_a) == 25:
        return True
    
    return False