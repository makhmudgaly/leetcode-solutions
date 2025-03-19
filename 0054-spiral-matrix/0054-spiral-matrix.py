class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = 0
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        
        up = left = 0
        right = n - 1
        down = m - 1

        
        while len(ans) < total:
            for col in range(left, right + 1):
                ans.append(matrix[up][col])
        
            for row in range(up + 1, down + 1):
                ans.append(matrix[row][right])
            
            if up != down:
                for col in range(right-1, left - 1, -1):
                    ans.append(matrix[down][col])
            if left != right:
                for row in range(down - 1, up, -1):
                    ans.append(matrix[row][left])
            
            up += 1
            down -= 1
            left += 1
            right -= 1
        
        return ans



