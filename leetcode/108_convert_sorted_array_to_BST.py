"""Completed 10 September 2024, 1 attempt"""


class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []: 
            return None 

        mid = len(nums) // 2

        my_bst = TreeNode(nums[mid])
        my_bst.left = self.sortedArrayToBST(nums[0:mid])
        my_bst.right = self.sortedArrayToBST(nums[mid+1:])

        return my_bst 