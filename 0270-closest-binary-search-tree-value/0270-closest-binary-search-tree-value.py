# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        return min(inorder(root), key=lambda x: abs(target - x))