class Solution(object):
    def isAnagram(self, s, t):
        # Quick length check
        if len(s) != len(t):
            return False
        
        # Count characters in both strings
        from collections import Counter
        return Counter(s) == Counter(t)
