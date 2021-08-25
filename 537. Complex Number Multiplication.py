class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        #split the nums into real and img
        num1 = a.split('+')
        num1[0], num1[1] = int(num1[0]), int(num1[1][:-1])
        num2 = b.split('+')
        num2[0], num2[1] = int(num2[0]), int(num2[1][:-1])
        real = [str(num1[0]*num2[0]-num1[1]*num2[1])] 
        img = [str(num1[0]*num2[1] + num1[1]*num2[0]) + 'i']
        ans = real + img
        return '+'.join(ans)   