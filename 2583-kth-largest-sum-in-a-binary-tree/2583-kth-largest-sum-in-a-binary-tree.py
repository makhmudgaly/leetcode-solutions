# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans = defaultdict(int)
        def traverse(root, level):
            if not root:
                return
            ans[level] += root.val
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        
        traverse(root, 0)
        
        values = sorted(list(ans.values()), reverse=True)
        return values[k-1] if len(values) >= k else -1