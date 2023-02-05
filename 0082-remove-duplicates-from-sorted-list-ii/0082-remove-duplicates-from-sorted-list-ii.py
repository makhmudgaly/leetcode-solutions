# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sent = ListNode(0, head)
        
        prev = sent
        
        while head != None:
            if head.next != None and head.val == head.next.val:
                while head.next != None and head.val == head.next.val:
                    head = head.next
                
                prev.next = head.next
            else:
                prev = prev.next
                
            head = head.next
        
        return sent.next