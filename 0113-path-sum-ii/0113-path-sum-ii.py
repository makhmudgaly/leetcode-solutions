# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root, curr_sum, path, ans, targetSum):
            if root:
                curr_sum += root.val
                if not root.left and not root.right and curr_sum == targetSum:
                    path.append(root.val)
                    ans.append(path)
                dfs(root.left, curr_sum, path + [root.val], ans, targetSum)
                dfs(root.right, curr_sum, path + [root.val], ans, targetSum)
        
        dfs(root, 0, [], ans, targetSum)
        
        return ans