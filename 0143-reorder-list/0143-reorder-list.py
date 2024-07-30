# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        stack = []
                
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        checkpoint = slow
        while slow.next != None:
            slow = slow.next
            stack.append(slow)
        
        slow = head
        fast = head
        while len(stack) > 0:
            fast = fast.next
            popped = stack.pop()
            slow.next = popped
            popped.next = fast
            slow = fast
            
        checkpoint.next = None
        
        
            
            
        