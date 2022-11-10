# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        head = test = ListNode()
        
        while list1 and list2:
            if list1.val<=list2.val:
                head.next = list1
                head = list1
                list1 = list1.next
            else:
                head.next = list2
                head = list2
                list2 = list2.next
                
        if list1:
            head.next = list1
            head = list1
            list1=list1.next
            
        if list2:
            head.next = list2
            head = list2
            list2 = list2.next
            
        return test.next

