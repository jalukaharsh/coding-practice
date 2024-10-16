"""Completed 9 September 2024, 1 attempt"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur_node = head
        new_head = Node(-1)
        new_node = new_head
        old_to_new = {}

        while cur_node is not None: 
            new_node.next = Node(cur_node.val)
            new_node = new_node.next 
            old_to_new[cur_node] = new_node
            if cur_node.random is None: 
                new_node.random = None
            cur_node = cur_node.next 
        
        new_node = new_head
        cur_node = head 
        while cur_node is not None: 
            new_node = new_node.next 
            if cur_node.random is not None: 
                new_node.random = old_to_new[cur_node.random]
            cur_node = cur_node.next 

        return new_head.next 
