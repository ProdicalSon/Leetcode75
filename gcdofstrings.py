class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        len1 = len(str1)
        len2 = len(str2)
        gcd_length = gcd(len1, len2)
        
        substring = str1[:gcd_length]
        if substring * (len1 // gcd_length) == str1 and substring * (len2 // gcd_length) == str2:
            return substring
        else:
            return ""

solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2)) 
