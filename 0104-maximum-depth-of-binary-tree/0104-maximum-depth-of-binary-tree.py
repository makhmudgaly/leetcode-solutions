# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        
        def visit(node, depth):
            if not node:
                return
            
            self.max_depth = max(depth, self.max_depth)
            visit(node.left, depth+1)
            visit(node.right, depth+1)
        
        visit(root, 1)
        return self.max_depth
            
        