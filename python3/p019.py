# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        items = [] # "cheating" but only up to 30 items in list anyways
        c = head
        while c:
            items.append(c)
            c = c.next

        before_index = len(items) - n - 1

        # special case: removing first item from list
        if n == len(items):
            return head.next

        # special case: removing last item from list
        if n == 1:
            items[before_index].next = None
            return head

        # normal case, update before to next item
        items[before_index].next = items[before_index+2]

        return head
