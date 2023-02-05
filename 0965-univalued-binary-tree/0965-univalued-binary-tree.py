# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def visit(node, prev):
            if not node:
                return True
            
            if node.val != prev:
                return False
            
            return visit(node.left, node.val) and visit(node.right, node.val)
        
        return visit(root, root.val)
        