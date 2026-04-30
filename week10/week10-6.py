# week10-6.py 學習計畫 Binary Tree - DFS 第5題
# LeetCode 1372. Longest ZigZag Path in a Binary Tree
# 找到中間 ZigZag 左右左右 or 右左右左 最長的那個
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # 整個的答案

        def helper(root):
            if root == None: return 0, 0 # 左邊最長、右邊最長

            Lans1, Lans2 = helper(root.left) # 左邊走，小朋友的左邊最長、右邊最長
            Rans1, Rans2 = helper(root.right)

            # 更新全局最大值：
            # 如果目前往左走，接的是左子樹的「右」路徑 (Lans2 + 1)
            # 如果目前往右走，接的是右子樹的「左」路徑 (Rans1 + 1)
            self.ans = max(self.ans, Lans2 + 1, Rans1 + 1)

            # 回傳給上一層：(目前的左邊最長, 目前的右邊最長)
            return Lans2 + 1, Rans1 + 1

        helper(root)
        return self.ans - 1
