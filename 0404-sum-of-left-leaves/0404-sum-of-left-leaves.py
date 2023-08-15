# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def traverse(root, is_left):
            nonlocal ans
            if root:
                if is_left and not root.left and not root.right:
                    ans += root.val
                
                traverse(root.left, True)
                traverse(root.right, False)
        
        traverse(root, False)
        return ans
            
            