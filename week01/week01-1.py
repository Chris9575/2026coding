#week01-1.py
#LeetCode 1404.Number of Steps to Reduce a Number in Binary Representation to One
class Solution:
    def numSteps(self, s: str) -> int:
        ans=0 #總共走幾步
        n=int(s,2)#把字串s當二進為整數變成n
        while n>1:#目標n最後變成1
            if n%2==0:n=n//2 #偶數//2
            else:n=n+1#基數+1
            ans+=1 #又多了一步
        return ans#總共要走幾步
