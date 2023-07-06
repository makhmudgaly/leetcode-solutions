# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(root):
            if not root:
                return False
            elif compare(root, subRoot):
                return True
            
            return traverse(root.left) or traverse(root.right)
        
        def compare(node1, node2):
            if not node1 or not node2:
                return node1 is None and node2 is None
            
            return (node1.val == node2.val) and compare(node1.left, node2.left) and compare(node1.right, node2.right)
        
        return traverse(root)
            