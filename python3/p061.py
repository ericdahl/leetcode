# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None

        # store linked list nodes in array for easier/faster logic
        # at expense of more memory
        l = []

        c = head
        while c:
            l.append(c)
            c = c.next

        # if k > len(l), don't "rotate" excessively
        k %= len(l)

        l = l[len(l) - k:len(l)] + l[0:len(l) - k]

        for i in range(len(l) - 1):
            l[i].next = l[i + 1]

        l[len(l) - 1].next = None

        return l[0]