# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def visit(node, min_val, max_val):
            if not node:
                return True
            
            if not min_val < node.val < max_val: 
                return False

            return visit(node.left, min_val, node.val) and visit(node.right, node.val, max_val)
        
        return visit(root, -inf, inf)
                
        
        
        