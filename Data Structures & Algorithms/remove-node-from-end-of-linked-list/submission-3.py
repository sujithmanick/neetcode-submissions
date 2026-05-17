# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        count = 1
        nh = ln= ListNode()

        while prev:
            if count == n:
                nh.next = prev.next
                break


            nh.next = prev
            nh = nh.next    
            count += 1  
            prev = prev.next

        ln = ln.next


        prev = None
        while ln:
            nxt = ln.next
            ln.next = prev
            prev = ln
            ln = nxt
                

        return prev