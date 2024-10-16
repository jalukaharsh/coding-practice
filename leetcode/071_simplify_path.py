"""Completed 10 September 2024, 1 attempt"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_lst = path.split('/')
        my_stack = []

        for subpath in path_lst: 
            if subpath == '..':
                if len(my_stack) > 0:
                    my_stack.pop()
            elif subpath == '': 
                continue 
            elif subpath == '.': 
                continue
            else: 
                my_stack.append(subpath)
        
        return '/' + '/'.join(my_stack)