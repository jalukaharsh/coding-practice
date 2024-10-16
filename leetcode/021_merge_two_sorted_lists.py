"""Completed 4 June 2024, 3 attempts"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lst_head = ListNode()

        if list1 is not None and list2 is not None: 
            if list1.val <= list2.val: 
                lst_head.val = list1.val
                list1 = list1.next
            else: 
                lst_head.val = list2.val 
                list2 = list2.next
            lst_head.next = self.mergeTwoLists(list1, list2)
        elif list1 is None and list2 is None: 
            lst_head = None
        elif list1 is None: 
            lst_head.val = list2.val
            lst_head.next = list2.next
        elif list2 is None: 
            lst_head.val = list1.val
            lst_head.next = list1.next

        return lst_head 



        while list1.val is not None and list2.val is not None: 
            next_node = ListNode()