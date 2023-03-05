# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # 1. Build up array of nodes
        nodes = []
        for l in lists:
            c = l
            while c:
                nodes.append(c)
                c = c.next

        if not nodes:
            return None

        # 2. Sort nodes in array by value
        nodes.sort(key=lambda n: n.val)

        # 3. Update next pointers based on new sorting
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[len(nodes) - 1].next = None

        return nodes[0]
