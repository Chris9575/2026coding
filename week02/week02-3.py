#week02-3.py 學習計畫
#392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1,N2=len(s),len(t)#字串的長度
        if N1==0: return True#如果左邊字串是空的,就不用比了
        i=0 #i從0開始
        for k in range(N2):#右邊一個個去試
            if s[i] == t[k]:#找到一個左右符和的
                i+=1#左邊的i往右生一級
            if i==N1:#左邊得i有走到右邊
                return True#成功
        #沒有走到最後,沒有比較成功
        return False#失敗
