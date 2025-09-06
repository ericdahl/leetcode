# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        nodes = []
        c = head
        while c:
            nodes.append(c)
            c = c.next

        for i in range(len(nodes)):
            if i % 2 == 0:
                continue

            nodes.insert(i, nodes.pop())


        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        head = nodes[0]
