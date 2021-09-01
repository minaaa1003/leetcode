#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        
        while left <= right:
        
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
# @lc code=end

