# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        unique = set()
        
        def traverse(node):
            if node:
                unique.add(node.val)
                traverse(node.left)
                traverse(node.right)
        
        traverse(root)
        
        local_min, ans = root.val, float("inf")
        
        for v in unique:
            if local_min < v < ans:
                ans = v
                
        return ans if ans < float("inf") else -1