# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root, ans):
            if not root:
                return
            
            stack = [(root,0)]
            
            while stack:
                node,level = stack.pop(0)
                ans[level].append(node.val)
                if node.left:
                    stack.append((node.left, level+1))
                if node.right:
                    stack.append((node.right, level+1))
        
        ans = defaultdict(list)
        bfs(root, ans)
        return ans.values()
        
        
        
            