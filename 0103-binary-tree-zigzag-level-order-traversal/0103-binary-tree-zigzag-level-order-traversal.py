# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        results = []
        queue = deque([root])
        left_to_right = True
    
        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                if left_to_right:
                    node = queue.popleft()
                    level_nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    level_nodes.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)

            results.append(level_nodes)
            left_to_right = not left_to_right

        return results