#week03-3.py學習計畫
#1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')#把5個字五變成set()
        count=0#紀錄目前有幾個母音
        for i in range(k):#找前面k個字母,逐一檢查
            if s[i] in vowels:count +=1#找到1個母音
        ans=count#離開迴圈時,確認前k個字母,有count個母音,先當答案
        N=len(s)#全部字串的長度
        for i in range(k,N):#右邊的每一個字母逐一檢查
            if s[i] in vowels: count+=1#右邊的投s[i]右吃到一個母音
            if s[i-k] in vowels: count-=1#左邊的尾巴s[i]吐掉一個母音
            ans=max(ans,count)#更新答案找到最大值
        return ans
