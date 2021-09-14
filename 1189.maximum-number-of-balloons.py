#
# @lc app=leetcode id=1189 lang=python
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        d = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for c in text:
            if c in d:
                d[c] += 1
        d["l"] //= 2
        d["o"] //= 2
        return min(d.values())
# @lc code=end

