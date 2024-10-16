"""Completed 3 July 2024, 1 attempt"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'], 
                    '4': ['g', 'h', 'i'], 
                    '5': ['j', 'k', 'l'], 
                    '6': ['m', 'n', 'o'], 
                    '7': ['p', 'q', 'r', 's'], 
                    '8': ['t', 'u', 'v'], 
                    '9': ['w', 'x', 'y', 'z']}

        possible_combs = []

        if digits == '': 
            return possible_combs 
        
        for letter in mapping[digits[0]]: 
            remaining_combs = self.letterCombinations(digits[1:])
            for comb in remaining_combs: 
                possible_combs.append(letter + comb) 
            if remaining_combs == []: 
                possible_combs.append(letter)
        
        return possible_combs