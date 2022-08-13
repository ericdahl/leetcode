# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def ll_to_list(head: Optional[ListNode]) -> list:

        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l

    @staticmethod
    def list_to_ll(l: list) -> Optional[ListNode]:

        ll_head = None
        ll_curr = None
        for c in l:
            new = ListNode(c)

            if not ll_head:
                ll_head = new
                ll_curr = new
                continue

            ll_curr.next = new
            ll_curr = new

        return ll_head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.ll_to_list(head)

        l = list(set(l))
        l.sort()

        return Solution.list_to_ll(l)