#week02-4 學習計畫
#11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0 #開始沒有答案
        i,j=0,len(height)-1 #左邊i,右邊j
        while i<j: #只要左右邊沒有撞再一起
            area=(j-i)*min(height[i],height[j])#算出現在的面積
            ans=max(ans,area)#更新答案
            if height[i]<height[j]:i+=1#小的i往右
            else:j-=1#小的j往左
        return ans
