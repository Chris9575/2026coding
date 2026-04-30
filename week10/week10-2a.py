#week10-2a.py學習計畫 Binary Search Tree
#LeetCode 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def helper(root):
            if root == None:return 0#沒有東西，深度0
            left=helper(root.left)#左邊的深度
            right=helper(root.right)#右邊的深度
            return max(left,right)+1
        return helper(root)
