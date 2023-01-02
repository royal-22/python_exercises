# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0
        while l1 or l2:
            n1, n2 = 0, 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2: 
                n2 = l2.val
                l2 = l2.next
            
            plus = n1 + n2 + carry
            res.next = ListNode(plus%10) #create node
            res, carry = res.next ,plus//10
        if carry:
            res.next = ListNode(carry)
        return dummy.next
