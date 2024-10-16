class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sequences = {}
        # for num in nums: 
        #     if num-1 in sequences: 
        #         sequences[num-1] = num
        #     if num+1 in sequences: 
        #         sequences[num] = num + 1
        #     else: 
        #         sequences[num] = None 
        
        # len_counter = 0
        # max_len = 0

        # for num in nums: 
        #     if num in sequences:
        #         len_counter = 1
        #     pos_key = num
        #     while sequences[pos_key] is not None:
        #         len_counter += 1
        #         pos_key = sequences[pos_key]
        #         sequences.pop(pos_key)
        #     while 
        #     if sequences[num] is not None: 
        #         len_counter += 1

        #         new_key = sequences[key]

        nums_set = set(nums) 

        sequence_counter = 0
        max_sequence = 0 

        for num in nums: 
            if num in nums_set:
                sequence_counter = 1
                nums_set.remove(num)
            pos_nums = num + 1
            while pos_nums in nums_set:
                sequence_counter += 1
                nums_set.remove(pos_nums)
                pos_nums += 1
            neg_nums = num - 1
            while neg_nums in nums_set: 
                sequence_counter += 1
                nums_set.remove(neg_nums)
                neg_nums -= 1
            if sequence_counter > max_sequence: 
                max_sequence = sequence_counter
            
        return max_sequence
