# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def append(head: Optional[ListNode],  tail: Optional[ListNode] , value) -> Tuple[ListNode, ListNode]:

        new = ListNode(value)

        if head == None:
            return (new, new)

        tail.next = new

        return (head, new)

    def list_to_int(l: Optional[ListNode]) -> int:
        multiplier = 1
        c = l
        s = 0
        while c:
            s += multiplier * c.val
            c = c.next
            multiplier *= 10
        return s



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        total = Solution.list_to_int(l1) + Solution.list_to_int(l2)

        (head, tail) = (None, None)

        # faster to use modulo arithmetic.. but simpler here
        for d in str(total)[::-1]:
            (head, tail) = Solution.append(head, tail, int(d))

        return head