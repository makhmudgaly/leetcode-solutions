# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(0)
        even = ListNode(0)
        p_odd = odd
        p_even = even
        
        is_odd = True
        
        while head:
            if is_odd:
                p_odd.next = head
                p_odd = p_odd.next
            else:
                p_even.next = head
                p_even = p_even.next
            
            head = head.next
            is_odd ^= True
            
        p_even.next = None
        p_odd.next = even.next
        return odd.next