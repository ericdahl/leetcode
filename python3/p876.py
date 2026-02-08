# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        c = head
        length = 0
        while c:
            length += 1
            c = c.next
        
        c = head
        for _ in range(length // 2):
            c = c.next
        return c
