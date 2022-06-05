# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def append(self, head: Optional[ListNode],  tail: Optional[ListNode] , value) -> Tuple[ListNode, ListNode]:

        new = ListNode(value)

        if head == None:
            return (new, new)

        tail.next = new

        return (head, new)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        head = None
        tail = None

        i = list1
        j = list2

        while i or j:

            while i and (not j or i.val <= j.val or not j):
                (head, tail) = self.append(head, tail,  i.val)
                i = i.next

            while j and (not i or j.val <= i.val or not i):
                (head, tail) = self.append(head, tail, j.val)
                j = j.next



        return head
