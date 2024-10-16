class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        valid_idx = 1
        prev_num = nums[0]
        duplicate_counter = 1

        for i in range(0, len(nums)): 
            if i and nums[i] != prev: 
                nums[valid_idx] = nums[i]
                valid_idx += 1
                duplicate_counter = 1
            elif i and nums[i] == prev: 
                duplicate_counter += 1 
                if duplicate_counter < 3: 
                    nums[valid_idx] = nums[i]
                    valid_idx += 1

            prev = nums[i]

        return valid_idx