from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # fine repeat words in str1 and str2.
        # use gcd method.

        # check valid string
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]