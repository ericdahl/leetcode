# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        
        while head and head.val == val:
            head = head.next

        if not head:
            return None


        a = head
        b = a.next

        while b:

            b = a.next
            while b and b.val == val:
                b = b.next
            a.next = b
            (a, b) = (b, a.next)

        return head
