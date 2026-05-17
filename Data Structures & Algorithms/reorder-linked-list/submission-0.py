# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer = head
        pointer2 = head.next
        while pointer2 and pointer2.next:
            pointer = pointer.next
            pointer2 = pointer2.next.next
        
        second_half = pointer.next
        pointer.next = None
        prev  = None
        while second_half:
            nex = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = nex
        
        temp1, temp2 = head, prev
        while temp2:
            t1 = temp1.next
            t2 = temp2.next

            temp1.next = temp2
            temp2.next = t1

            temp1 = t1
            temp2 = t2


        

        