class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_min = 10e4
        cur_max = 0 
        profit_so_far = 0 

        for price in prices: 
            if price < cur_max: 
                profit_so_far += cur_max - cur_min 
                cur_min = price 
                cur_max = price 
            if price < cur_min:
                if cur_max - cur_min > 0: 
                    profit_so_far += cur_max - cur_min 
                cur_min = price
                cur_max = price
            elif price > cur_max: 
                cur_max = price 
        profit_so_far += cur_max - cur_min 
        return profit_so_far 