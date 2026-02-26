#week01-3.py
#LeetCode 1071. Greatest Common Divisor of Strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N1,N2=len(str1),len(str2)#兩個字串長度
        N=gcd(N1,N2)#最大公因數
        ans=str1[:N]#字串1的前面N個字母

        if ans*(N1//N) != str1:return""#不符和就失敗
        if ans*(N2//N) != str2:return""
        return ans
