# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent_to_children = defaultdict(list)
        all_nodes = set()
        children = set()
        
        for parent, child, is_left in descriptions:
            parent_to_children[parent].append((child, is_left))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)
        
        root = (all_nodes - children).pop()
        
        def build(val):
            node = TreeNode(val)
            
            if val in parent_to_children:
                for child, is_left in parent_to_children[val]:
                    if is_left:
                        node.left = build(child)
                    else:
                        node.right = build(child)
            
            return node
        
        return build(root)