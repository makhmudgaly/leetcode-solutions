# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        res = ListNode()
        curr_sum = 0
        carry = 0
        
        while s1 or s2:
            if s1:
                curr_sum += s1.pop()
            if s2:
                curr_sum += s2.pop()
                
            res.val = curr_sum % 10
            carry = curr_sum // 10
            head = ListNode(carry)
            head.next = res
            res = head
            curr_sum = carry
        
        return res.next if carry == 0 else res