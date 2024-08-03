class Solution:
    def validUtf8(self, data: List[int]) -> bool:
            
        def format_binary(a, total_length=8):
            binary_representation = bin(a)[2:]
            padding_length = total_length - len(binary_representation)
            padded_binary = '0' * padding_length + binary_representation
            return padded_binary
        
        n_bytes = 0
        for num in data:
            binary = format_binary(num)
            
            if n_bytes == 0:
                for bit in binary:
                    if bit == '0':
                        break
                    n_bytes += 1
                
                if n_bytes == 0:
                    continue
                
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not(binary[0] == '1' and binary[1] == '0'):
                    return False
            
            n_bytes -= 1
        
        
        return n_bytes == 0