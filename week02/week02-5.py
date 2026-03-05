#week02-5.py 學習計畫
#1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()#小到大排好,等一下左邊挑一個右邊挑一個看能不能排列
        ans=0
        i,j=0,len(nums)-1#最左邊i對應最小,最右邊j對應最大
        while i<j:#還沒有撞再一起就可以左右個挑一個
            if nums[i]+nums[j]==k:
                ans+=1
                i,j=i+1,j-1#右邊用了往右邊,左邊用了往左邊
            if nums[i]+nums[j] <k:#加起來太小了,那左邊小的i
                ｉ+=1
            if nums[i]+nums[j] > k:#加起來大了,那右邊小的j
                ｊ-=1
        return ans
