# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # 1. convert list to array
        nodes = []
        c = head
        while c:
            nodes.append(c)
            c = c.next

        # 2. create new array reversing groups
        new_nodes = []
        while nodes:
            t = nodes[0:k]

            nodes = nodes[k:]
            if k <= len(t):
                t.reverse()
            new_nodes += t

        # 3. update node pointers
        for i in range(len(new_nodes) - 1):
            new_nodes[i].next = new_nodes[i + 1]


        new_nodes[len(new_nodes) - 1].next = None

        return new_nodes[0]
