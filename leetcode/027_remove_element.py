class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_len = len(nums)
        val_set = []
        for i in range(0, len(nums)): 
            if nums[i] == val: 
                val_set.append(i)
        swap_counter = len(nums) - 1
        print(val_set)
        val_occurences = len(val_set) 
        for i in range(0, len(val_set)): 
            cur_idx = val_set[i]
            while swap_counter == cur_idx or swap_counter in val_set: 
                swap_counter -= 1
            nums[cur_idx] = nums[swap_counter]
            swap_counter -= 1

        return nums_len - val_occurences