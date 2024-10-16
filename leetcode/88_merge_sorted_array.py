class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        m_counter = m - 1
        n_counter = n - 1
        i = m + n - 1

        while i >= 0 and n_counter >= 0:
            if nums1[m_counter] >= nums2[n_counter] and m_counter >= 0: 
                nums1[i] = nums1[m_counter]
                nums1[m_counter] = 0
                m_counter -= 1
            else: 
                nums1[i] = nums2[n_counter]
                n_counter -= 1
            i -= 1

        