# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        
        def visit(root, ans):
            if not root:
                return
            
            ans.append(root.val)
            visit(root.left, ans)
            visit(root.right, ans)
            
        visit(root1, ans)
        visit(root2, ans)
        
        return sorted(ans)
        