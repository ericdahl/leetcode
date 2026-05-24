# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left_head, left_tail, right_head, right_tail = None, None, None, None
        
        c = head
        while c:
            if c.val < x:
                if not left_head:
                    left_head = c
                    left_tail = c
                else:
                    left_tail.next = c
                    left_tail = c
            else:
                if not right_head:
                    right_head = c
                    right_tail = c
                else:
                    right_tail.next = c
                    right_tail = c
            c = c.next

        if right_tail:
            right_tail.next = None

        if left_tail:
            left_tail.next = right_head

        if left_head:
            return left_head
        return right_head # special case of nothing in left
        
