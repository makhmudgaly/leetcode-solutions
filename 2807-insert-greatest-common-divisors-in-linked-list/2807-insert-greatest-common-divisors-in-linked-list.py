# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = head
        if not head or not head.next:
            return head
        
        while curr and curr.next:
            prev = curr
            if curr.next:
                curr = curr.next
            x = prev.val
            y = curr.val
            gcd = math.gcd(x,y)
            new_node = ListNode(gcd)
            prev.next = new_node
            new_node.next = curr
        
        return head
            
            