#
# @lc app=leetcode id=633 lang=python
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # using sqrt funciton: 
        # if (c - a^2) is an int, then b exists
        for a in range(int(sqrt(c))+1):
            b = sqrt(c-a*a)
            if b == int(b):
                return True
        return False
                        
                
# @lc code=end

