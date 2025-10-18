# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def zero_vals(vals: List[int]) -> None:
        max_val = -1
        for i in range(len(vals) - 1, -1, -1):
            if vals[i] < max_val:
                vals[i] = 0
            max_val = max(max_val, vals[i])

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        vals = []
        c = head
        while c:
            vals.append(c.val)
            c = c.next

        Solution.zero_vals(vals)


        c = head

        for v in vals[:-1]:
            if v > 0:
                c.val = v
                c = c.next
        if vals[-1] > 0:
            c.val = vals[-1]
        c.next = None
        return head