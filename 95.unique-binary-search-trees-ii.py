#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # We can use dp technique here, 
        # where in dp[i][j] we keep all possible trees 
        # from numbers i ... j. We can also keep only 
        # ne dimensional dp, but then we need to clone trees, 
        # adding the same values to all elements. 
        # However, number of trees is exponential, 
        # and I think it is not worth to make this optimization 
        # from O(n^2) to O(n) memory, because problem can be 
        # solved for only small n <= 50.
        def dp(i, j):
            if i > j: return [None]
            ans = []
            
            for k in range(i, j + 1):
                for lft, rgh in product(dp(i, k-1), dp(k+1, j)):
                    root = ListNode(k)
                    root.left = lft
                    root.right = rgh
                    ans.append(root)            
            return ans
        
        return dp(1, n)
        
# @lc code=end

