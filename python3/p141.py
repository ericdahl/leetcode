# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def hasCycle_cheat(self, head: Optional[ListNode]) -> bool:
        return "cycle" in str(head)


    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = {}

        c = head
        while c:
            if c in seen:
                return True
            seen[c] = True
            c = c.next

        return False
