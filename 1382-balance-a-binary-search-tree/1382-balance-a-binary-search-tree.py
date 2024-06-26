# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        traversal = []
        self.traverse(root, traversal)
        return self.create_tree(traversal, 0, len(traversal) - 1)
    
    def traverse(self, root: TreeNode, inorder: list):
        if not root:
            return 
        
        self.traverse(root.left, inorder)
        inorder.append(root.val)
        self.traverse(root.right, inorder)
    
    def create_tree(self, inorder: list, start, end):
        if start > end:
            return None
        
        mid = start + (end - start) // 2
        left = self.create_tree(inorder, start, mid - 1)
        right = self.create_tree(inorder, mid + 1, end)
        
        node = TreeNode(inorder[mid], left, right)
        return node