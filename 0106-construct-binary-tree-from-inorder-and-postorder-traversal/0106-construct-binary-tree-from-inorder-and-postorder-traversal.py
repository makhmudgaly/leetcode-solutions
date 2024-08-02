# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postIdx = len(postorder) - 1
        m = {num:idx for idx,num in enumerate(inorder)}
        
        def build(lo,hi):
            if lo > hi:
                return None
            
            root = TreeNode(postorder[self.postIdx])
            self.postIdx -= 1
            
            mid = m.get(root.val)
            root.right = build(mid + 1, hi)
            root.left = build(lo, mid - 1)
            
            return root
        
        return build(0, len(inorder)-1)