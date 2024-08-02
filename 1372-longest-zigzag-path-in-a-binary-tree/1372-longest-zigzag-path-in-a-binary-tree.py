# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        self.dfs(root, False, 0)
        self.dfs(root, True, 0)
        
        return self.max_length
        
    def dfs(self, node, goLeft, length):
        if not node:
            return
        
        self.max_length = max(self.max_length, length)
        # to go left
        if goLeft:
            self.dfs(node.left, not goLeft, length + 1)
            self.dfs(node.right, goLeft, 1)
        else:
            self.dfs(node.left, goLeft, 1)
            self.dfs(node.right, not goLeft, length + 1)
        