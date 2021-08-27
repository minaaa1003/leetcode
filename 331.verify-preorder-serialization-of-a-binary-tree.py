#
# @lc app=leetcode id=331 lang=python
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        # Trick using slots - 
        # every non-null node creates 2 slots and consumes 1 slot -> +2-1
        # every null node creates 0 slot and consumes 1 slot -> -1
        # slots num starts with a slot for the node itself -> 1
        nodes = preorder.split(",")
        slots = 1
        for node in nodes:
            # leaving no space for new nodes -> not balanced
            if slots <= 0:
                return False
            
            slots += -1 if node == '#' else 1

        # Preorder satisfied if final slots == 0    
        return slots == 0
# @lc code=end

