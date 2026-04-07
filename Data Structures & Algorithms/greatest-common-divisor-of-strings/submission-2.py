class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(num1, num2):
            if not num2: return num1
            return gcd(num2, num1%num2)
        l = gcd(len(str1), len(str2))
        x = len(str1) // l
        y = len(str2) // l
        return "" if str2[:l] * x != str1 or str1[:l] * y != str2 else str1[:l]