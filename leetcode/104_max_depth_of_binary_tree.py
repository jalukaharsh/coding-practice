"""Completed 6 June 2024, 1 attempt"""


class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth_so_far = 0
        if root is None: 
            return depth_so_far
        elif root.left is None and root.right is None: 
            depth_so_far += 1
            return depth_so_far
        else: 
            depth_so_far += 1
            sol = Solution()
            max_left = sol.maxDepth(root.left) 
            max_right = sol.maxDepth(root.right)
            depth_so_far += max(max_left, max_right)

        return depth_so_far
