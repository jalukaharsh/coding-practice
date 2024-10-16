class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies_given_l2r = [1 for _ in ratings]
        candies_given_r2l = [1 for _ in ratings]

        for i in range(0, len(ratings)-1): 
            if ratings[i] < ratings[i+1]:
                candies_given_l2r[i+1] = candies_given_l2r[i] + 1

        for i in range(0, len(ratings)-1):
            j = len(ratings) - i - 1
            if ratings[j] < ratings[j-1]:
                candies_given_r2l[j-1]  = candies_given_r2l[j] + 1
        candies_given = [max(l2r, r2l) for l2r, r2l in zip(candies_given_l2r, candies_given_r2l)]
        return sum(candies_given)
