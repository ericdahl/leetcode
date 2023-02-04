# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def build_list(head: Optional[ListNode]):
        nodes = []
        c = head
        while c:
            nodes.append(c)
            c = c.next

        return nodes

    @staticmethod
    def swap_list(node_list):
        i = 0
        while i < len(node_list) - 1:
            node_list[i], node_list[i + 1] = node_list[i + 1], node_list[i]
            i += 2



    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node_list = Solution.build_list(head)

        Solution.swap_list(node_list)


        for n in node_list:
            n.next = None

        if not node_list:
            return head

        head = node_list.pop(0)

        c = head
        while len(node_list) > 0:
            new_c = node_list[0]
            c.next = node_list.pop(0)
            c = new_c
        return head

