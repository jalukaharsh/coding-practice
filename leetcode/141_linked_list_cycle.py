"""Completed 6 June 2024, 2 attempts"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        i = 0 
        nodes_so_far = set()
        if head is None: 
            return False 
            
        while head.next is not None: 
            if head.next in nodes_so_far: 
                return True 
            else: 
                nodes_so_far.add(head.next)
                head = head.next
        return False