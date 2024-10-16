class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_window = ''
        candidate_len = 0 

        for i in range(0, len(s)): 
            if s[i] in cur_window: 
                while s[i] in cur_window: 
                    cur_window = cur_window[1:]
            cur_window += s[i] 
            if len(cur_window) > candidate_len: 
                candidate_len = len(cur_window)
        
        return candidate_len