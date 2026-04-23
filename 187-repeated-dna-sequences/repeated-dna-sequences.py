from collections import Counter

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        freq = {}
        
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            
            if sub in freq:
                freq[sub] += 1
            else:
                freq[sub] = 1
        
        ans = []
        
        for key in freq:
            if freq[key] > 1:
                ans.append(key)
        
        return ans