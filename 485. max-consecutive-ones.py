class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, cnt, lastNum = 0, 0, -1
        for num in nums:
            if lastNum != num:
                lastNum = num
                cnt = 1
            else:
                cnt += 1
                
            if num == 1:
                ans = max(ans, cnt)
        return ans
