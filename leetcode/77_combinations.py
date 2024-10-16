"""Completed 9 September 2024, 1 attempt"""


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        possible_combs_1 = []
        if k == 1: 
            for i in range(1, n+1):
                possible_combs_1.append([i])
            return possible_combs_1

        possible_combs = []
        for i in range(0, n): 
            j = n - i 
            result = self.combine(j-1, k-1) 
            for item in result: 
                item.append(j) 
                possible_combs.append(item)
        return possible_combs
