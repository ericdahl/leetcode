# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        visited = set()
        a = headA
        while a:
            visited.add(a)
            a = a.next

        b = headB
        while b:
            if b in visited:
                return b
            b = b.next

        return None