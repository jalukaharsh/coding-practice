class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_anagrams = {}

        for word in strs: 
            sorted_word = ''.join(sorted(word))
            if sorted_word in sorted_anagrams:
                sorted_anagrams[sorted_word].append(word)
            else:
                sorted_anagrams[sorted_word] = [word]
        
        return sorted_anagrams.values()
