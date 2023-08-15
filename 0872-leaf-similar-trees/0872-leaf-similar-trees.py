# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_one = []
        leaf_two = []
        
        def traverse(root, leafs):
            if root:
                if not root.left and not root.right:
                    leafs.append(root.val)
                traverse(root.left, leafs)
                traverse(root.right, leafs)
        
        traverse(root1, leaf_one)
        traverse(root2, leaf_two)
        
        return leaf_one == leaf_two