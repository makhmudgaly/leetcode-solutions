# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def visit(root, curr):
            if root:
                if not root.left and not root.right:
                    curr = curr * 10 + root.val
                    self.ans += curr

                visit(root.left, curr*10 + root.val)  
                visit(root.right, curr*10 + root.val)
        
        visit(root, 0)
        return self.ans
            
            
        