# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        rem = 0
        dummy = head = ListNode()
        while l1 and l2:
            rem += l1.val + l2.val
            node = ListNode(rem%10)
            rem //= 10
            head.next = node
            head = head.next
            l1 = l1.next
            l2 = l2.next
            rem %= 10
            
        while l1:
            rem += l1.val
            node = ListNode(rem%10)
            rem //= 10
            head.next = node
            head = head.next
            l1 = l1.next
        
        while l2:
            rem += l2.val
            node = ListNode(rem%10)
            rem //= 10
            head.next = node
            head = head.next
            l2 = l2.next
        
        if rem:
            head.next = ListNode(rem)
            
        return dummy.next