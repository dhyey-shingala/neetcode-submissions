class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [i for i in s]
        s2 = [i for i in t]

        s1.sort()
        s2.sort()

        if s1 == s2:
            return True
        return False