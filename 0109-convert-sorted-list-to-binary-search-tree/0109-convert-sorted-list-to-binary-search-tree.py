# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.arr = []
        while head != None:
            self.arr.append(head.val)
            head = head.next
        
        return self.buildTree(self.arr)
    
    def buildTree(self, l):
        if l==[] or l==None:
                return
        elif len(l)==1:
            return TreeNode(l[0])
        mid = (len(l)) // 2
        
        root = TreeNode(l[mid])
        root.left = self.buildTree(l[:mid])
        root.right = self.buildTree(l[mid+1:])
        
        return root
    
            
        