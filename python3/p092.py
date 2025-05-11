# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        head_left = head

        # find start node for reversing
        for _ in range(left - 1):
            head_left = head_left.next

        # build stack of values to be reversed
        node = head_left
        stack = []
        for _ in range(right - left + 1):
            stack.append(node.val)
            node = node.next

        # reset back to start node and set values
        node = head_left
        for _ in range(right - left + 1):
            node.val = stack.pop()
            node = node.next

        return head