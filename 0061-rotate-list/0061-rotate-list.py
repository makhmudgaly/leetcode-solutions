# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        start = head
        last = head
        temp = head
        
        length = 1
        while last.next:
            length += 1
            last = last.next
        
        k = k % length
        
        if (k == 0 and length > 1) or k == length:
            return head
        
        last.next = head
        
        for i in range(length - k):
            temp = start
            start = start.next
        
        start = temp.next
        temp.next = None
        
        return start