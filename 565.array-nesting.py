#
# @lc app=leetcode id=565 lang=python
#
# [565] Array Nesting
#

# @lc code=start
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if the node is not visited, we dfs() it to find the cycle
        n = len(nums)
        visited = [False] * n
        ans = 0
        for x in nums:
            cnt = 0
            while not visited[x]:
                #increasing the size of the cycle
                cnt += 1
                visited[x] = True
                x = nums[x]
            #keep updating the ans
            ans = max(ans, cnt)
                
        return ans
# @lc code=end

