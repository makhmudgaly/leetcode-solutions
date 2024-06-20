# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        d = defaultdict(int)
        
        def traverse(root):
            if not root:
                return
            
            d[root.val] += 1
            
            
            return traverse(root.left) or traverse(root.right)
        
        traverse(root)
        max_freq = max(d.values())
        for key in d:
            if d[key] == max_freq:
                ans.append(key)
        
        return ans
        