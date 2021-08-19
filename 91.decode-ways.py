#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0]*(len(s)+1)
        
        dp[0]=1
        if s[0] !='0':
            dp[1]=1
            
        for i in range(2,len(s)+1):
            if s[i-1]!='0':
                dp[i] += dp[i-1]
                
            if s[i-2] == '0':
                continue
            
            n = s[i-2]+s[i-1]
            if ('1' <= n <= '26'):
                dp[i] += dp[i-2]
                
        
        return dp[-1]
# @lc code=end

