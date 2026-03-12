#week03-5厩策璸礶
#1493. Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N=len(nums)#皚
        zeros=0#矰砰ずΤぶ0
        tail=0#矰Юぺ程秨﹍
        ans=0#矰程
        for head in range (N):#矰繷硋┕
            if nums[head]==0:zeros+=1#狦Τ瑀0,zeros+1
            while zeros >1:#Τ瑀0び
                if nums[tail]==0:zeros-=1#狦┰▄┰Τ瑀0,zeros-1
                tail+=1#Юぺぇ罽
            ans=max(ans,head-tail+1)#穝矰程ㄎ
        return ans-1#肈ヘ弧﹚璶浪1
