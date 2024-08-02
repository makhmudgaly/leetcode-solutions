# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mx, mn):
            if not root:
                return abs(mx-mn)
            
            mx = max(mx, root.val)
            mn = min(mn, root.val)
            
            return max(dfs(root.left, mx, mn), dfs(root.right, mx, mn))
        
        return dfs(root, float("-inf"), float("inf"))