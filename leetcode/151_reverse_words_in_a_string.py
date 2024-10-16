class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst_words = s.split()
        reversed_s = ''
        while lst_words != []: 
            reversed_s += lst_words.pop() + ' ' 
        
        return reversed_s[:-1]