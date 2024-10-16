"""Completed 6 June 2024, 1 attempt"""

class Node(object): 
    def __init__(self, val, cur_min): 
        self.val = val
        self.cur_min = cur_min


class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.stack == []: 
            new_node = Node(val, val)
        else: 
            prev_node = self.stack[-1]
            new_node = Node(val, min(val, prev_node.cur_min))
        
        self.stack.append(new_node)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1].cur_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()