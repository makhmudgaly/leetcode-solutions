# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(0)
        new_head.next = head
        slow = fast = new_head
        
        while n > 0:
            fast = fast.next
            n-=1
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return new_head.next