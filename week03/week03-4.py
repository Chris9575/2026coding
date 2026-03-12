#week03-4.py 學習計畫
#1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=0#一開始沒有0
        N=len(nums)#陣列的長度
        ans=0#最終長度
        tail=0#尾巴從0開始
        for head in range(N):#頭往右吃
            if nums[head]==0:#吃到1顆0
                zeros+=1#體內0增加
                #if zeros>k:#超過體內可以擁有的0,要吐出0
                while zeros>k:#要用while一直吐出的0
                    if nums[tail]==0:#現在尾巴吐出0
                        zeros-=1#0減少
                    tail+=1#長度要增加1
            ans=max(ans,head-tail+1)#更新答案
        return ans
