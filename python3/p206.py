# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # no memory constraint so just use an array
        arr = []
        
        c = head
        while c:
            arr.append(c)
            c = c.next

        for c_idx, c in enumerate(arr):
            if c_idx == 0:
                c.next = None
                continue

            c.next = arr[c_idx - 1]

        return arr[-1]
