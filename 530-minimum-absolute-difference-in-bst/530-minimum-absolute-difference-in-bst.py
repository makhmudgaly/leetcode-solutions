# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []
        def visit(root):
            if not root:
                return
            
            visit(root.left)
            ans.append(root.val)
            visit(root.right)
        
        visit(root)
        
        return min(b - a for a, b in zip(ans, ans[1:]))
        