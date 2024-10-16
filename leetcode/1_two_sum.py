class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remainders_dict = {}
        indices = [0, 0]
        for i in range(0, len(nums)):
            if nums[i] in remainders_dict: 
                indices = [i, remainders_dict[nums[i]]]
            else: 
                remainders_dict[target-nums[i]] = i 

        return indices
