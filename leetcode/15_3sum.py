class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums.sort()

        for i, num in enumerate(nums): 
            if (i == 0) or nums[i] != nums[i-1]: 
                l = i + 1
                r = len(nums) - 1
                while l < r: 
                    triple_sum = nums[l] + nums[r] + num
                    if triple_sum == 0: 
                        if r == len(nums)-1 or (nums[l] != nums[l-1] or nums[r] != nums[r+1]):
                            triplets.append([nums[l], nums[r], num])
                        l += 1
                        r -= 1
                    else: 
                        if triple_sum > 0:
                            r -= 1
                        else: 
                            l += 1
        
        return triplets
