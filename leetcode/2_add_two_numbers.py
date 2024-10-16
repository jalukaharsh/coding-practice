"""Completed 8 September 2024, 1 attempt"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_num = 0 
        second_num = 0 
        factor = 1
        while l1 is not None: 
            first_num += l1.val * factor 
            l1 = l1.next
            factor *= 10 
        factor = 1
        while l2 is not None: 
            second_num += l2.val * factor 
            l2 = l2.next 
            factor *= 10 
        
        final_val = first_num + second_num 
        factor = 10 
        final_lst = ListNode(final_val % factor)
        final_val = final_val // factor
        prev_node = final_lst

        while final_val > 0: 
            cur_node = ListNode()
            prev_node.next = cur_node
            lst_val = final_val % factor
            final_val = final_val // factor
            cur_node.val = lst_val
            prev_node = cur_node 
        
        return final_lst 