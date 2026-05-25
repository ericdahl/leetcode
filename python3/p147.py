# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_list = head
        old_list = head.next
        new_list.next = None

        while old_list:
            old_list_next = old_list.next

            prior = None
            c = new_list
            while c and c.val < old_list.val:
                prior = c
                c = c.next

            if not prior:
                new_list = old_list
            else:
                prior.next = old_list
            
            old_list.next = c
            old_list = old_list_next

        return new_list

        
