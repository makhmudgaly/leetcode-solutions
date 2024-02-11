class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for j in range(len(matrix[0])):
            max_el = matrix[0][j]
            neg_el_idxs = []
            for i in range(len(matrix)):
                max_el = max(max_el, matrix[i][j])
                if matrix[i][j] == -1:
                    neg_el_idxs.append(i)
            
            for idx in neg_el_idxs:
                matrix[idx][j] = max_el
        
        return matrix
                