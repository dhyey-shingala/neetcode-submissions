class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for w in s:
            if w.isalnum():
                s1 = s1 + w

        s1 = s1.lower()

        if s1 == s1[::-1]:
            return True

        return False