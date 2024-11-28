# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None


        def insert(head: TreeNode, left: List[int], right: List[int]):
            if not head:
                return

            if left:
                left_mid = left[len(left) // 2]
                left_left = left[0:len(left) // 2]
                left_right = left[len(left) // 2 + 1:]

                head.left = TreeNode(left_mid)
                insert(head.left, left_left, left_right)

            if right:
                right_mid = right[len(right) // 2]
                right_left = right[0:len(right) // 2]
                right_right = right[len(right) // 2 + 1:]
                head.right = TreeNode(right_mid)
                insert(head.right, right_left, right_right)



        l = []
        while head:
            l.append(head.val)
            head = head.next

        left = l[0:len(l) // 2]
        mid = l[len(l) // 2]
        right = l[len(l) // 2 + 1:]

        root = TreeNode(mid)
        insert(root, root, left, right)

        return root
