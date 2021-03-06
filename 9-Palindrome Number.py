'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''

#by myself
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            if x == int(''.join((reversed(str(x))))):
                return True
            else:
                return False
# by myself            
class Solution:
    def isPalindrome(self, x):
        r = list(str(x))
        length = len(r)
        if length <= 2:
            return r[0] == r[-1]
        for i in range(length // 2 + 1):
            if r[i] == r[-(i+1)]:
                pass
            else:
                return False
        return True
    
# others
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x != int(str(x)[::-1]):
            return False
        else:
            return True

# by others
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
