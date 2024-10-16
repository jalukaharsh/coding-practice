"""Completed 3 July 2024, 2 attempts"""


class Solution(object):
    def __init__(self): 
        self.ways_at_n = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways_so_far = 0
        if n == 1: 
            return 1
        elif n == 2: 
            return 2
        else: 
            if n-1 not in self.ways_at_n: 
                self.ways_at_n[n-1] = self.climbStairs(n-1)
            self.ways_at_n[n-2] = self.climbStairs(n-2)
            ways_so_far += self.ways_at_n[n-1]
            ways_so_far += self.ways_at_n[n-2]
            return ways_so_far