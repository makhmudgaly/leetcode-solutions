class Solution:
    def calculate(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        
        stack = []
        current_number = 0
        operation = '+'
        result = 0
        for i in range(length):
            current_char = s[i]
            if current_char.isdigit():
                current_number = current_number * 10 + int(current_char)
            
            if not current_char.isdigit() and not current_char == ' ' or i == length - 1:
                if operation == '-':
                    stack.append(-current_number)
                elif operation == '+':
                    stack.append(current_number)
                elif operation == '*':
                    top = stack.pop()
                    stack.append(top * current_number)
                elif operation == '/':
                    top = stack.pop()
                    stack.append(math.trunc(top / current_number))
                
                operation = current_char
                current_number = 0
                
        while stack:
            result += stack.pop()
        
        return result
