# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast =  slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            tmp = curr.next

            curr.next = prev

            prev = curr
            
            curr = tmp

        
        

        curr2 = head
        scd = prev
        while scd:
            tmp = curr2.next
            tmp2 = scd.next

            curr2.next = scd
            scd.next = tmp

            curr2 = tmp
            scd = tmp2



