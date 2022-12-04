# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        # note: not using ideal O(1) space here. fast/slow iteration can be used for O(1)
        l = []
        n = head
        while n:
            l.append(n.val)
            n = n.next

        return l == l[::-1]
