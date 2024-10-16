"""Completed 10 September 2024, 1 attempt"""

class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: 
            return None
        
        inverted_tree = TreeNode(root.val)
        inverted_tree.left = self.invertTree(root.right)
        inverted_tree.right = self.invertTree(root.left) 

        return inverted_tree