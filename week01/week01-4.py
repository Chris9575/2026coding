#week01-4.py
#LeetCode 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]#答案的True和False將含在裡面
        best=max(candies)#目前小朋友最多有幾個糖
        for candie in candies:#逐一檢查、如果把extraCandies 給小朋友
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False)#他會不會 >= 最多的,依序置入ans
        return ans
