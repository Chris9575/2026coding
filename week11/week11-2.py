# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# week11-2.py 學習計畫 Binary Tree - DFS 第2題 Easy題
# LeetCode 236. Lowest Common Ancestor of a Binary Tree (原圖標註為 872 延伸練習)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = []
        def helper(root):
            if root == None: return 0
            left = helper(root.left)
            right = helper(root.right)
            mid = 1 if root == p or root == q else 0
            if left + right + mid == 2:
                a.append(root)
            return left + right + mid

        helper(root)
        return a[0]
