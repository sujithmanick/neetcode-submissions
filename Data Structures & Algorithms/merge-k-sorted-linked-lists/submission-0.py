# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergetwolist(self, l1, l2):
        dummy= curr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(val=l1.val)
                curr = curr.next
                l1 = l1.next
            elif l1.val > l2.val:
                curr.next = ListNode(val=l2.val)
                curr = curr.next
                l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while lists and len(lists) > 1:
            mergedlists = []
            for i in range(0,len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedlists.append(self.mergetwolist(list1, list2))
            lists = mergedlists

        return lists[0]





