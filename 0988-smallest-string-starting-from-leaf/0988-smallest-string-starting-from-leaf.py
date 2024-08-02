# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
       
            
        self.ans = ""
        
        def dfs(root, word):
            if not root:
                return
            
            word = chr(ord('a')+root.val) + word
            
            if not root.left and not root.right:
                if not self.ans or self.ans > word:
                    self.ans = word
            if root.left:
                dfs(root.left, word)
            if root.right:
                dfs(root.right, word)
        
        dfs(root, "")
        
        return self.ans