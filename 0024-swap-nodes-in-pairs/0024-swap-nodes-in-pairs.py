# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        slow = head
        fast = head
        dummy = ListNode(-101, head)
        tmp = dummy
        while fast != None and fast.next != None:
            fast = fast.next
            tmp2 = fast.next
            tmp.next = fast
            fast.next = slow
            slow.next = tmp2
            fast = tmp2
            tmp = slow
            slow = tmp2
            
        return dummy.next