"""Completed 6 June 2024, 4 attempts"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_stack = []
        validity = False
        for char in s: 
            if char in {'(', '{', '['}: 
                if char == '(': 
                    my_stack.append(')')
                elif char == '{': 
                    my_stack.append('}')
                else: 
                    my_stack.append(']')
            else:  # assuming input string is valid
                if len(my_stack) > 0: 
                    validity = (char == my_stack[-1])
                    if validity: 
                        my_stack.pop()
                    else: 
                        return validity
                else: 
                    validity = False
                    return validity
        if len(my_stack) == 0: 
            return validity
        else: 
            return False