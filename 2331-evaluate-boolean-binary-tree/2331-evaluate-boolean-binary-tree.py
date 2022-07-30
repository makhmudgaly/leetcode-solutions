# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def visit(root):
            if(root.left==None and root.right==None):
                return root.val
            elif root.val==2:
                return visit(root.left)or visit(root.right)
            return visit(root.left) and visit(root.right)
            
        return visit(root)
        