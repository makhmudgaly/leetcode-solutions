"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def dfs(root, lvl):
            if not root:
                return
            
            if lvl == len(ans):
                ans.append([])
            ans[lvl].append(root.val)
            for child in root.children:
                dfs(child, lvl + 1)
                
        ans = []
        dfs(root,0)
        return ans