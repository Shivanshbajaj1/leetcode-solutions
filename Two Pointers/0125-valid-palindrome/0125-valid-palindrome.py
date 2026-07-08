class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        l = len(cleaned)

        for i in range(l // 2):
            if cleaned[i] != cleaned[l - i - 1]:
                return False

        return True