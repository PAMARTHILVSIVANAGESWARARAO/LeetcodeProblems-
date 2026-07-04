class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        # Find the shorter length to avoid IndexErrors
        min_len = min(len(word1), len(word2))
        
        # Alternately append characters up to the shorter length
        for i in range(min_len):
            res += word1[i]
            res += word2[i]
            
        # Append the remaining characters from the longer string
        res += word1[min_len:]
        res += word2[min_len:]
        
        return res
