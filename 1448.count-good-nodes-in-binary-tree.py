#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        if not root: return 0

        def dfs(cur, val):
            #val keeps track of the current largest value
            if cur.val >= val: self.count += 1
            #keep going if there is a left or right child
            if cur.left: dfs(cur.left, max(val, cur.val))
            if cur.right: dfs(cur.right, max(val, cur.val))
        
        dfs(root, root.val)
        return self.count
        
# @lc code=end

