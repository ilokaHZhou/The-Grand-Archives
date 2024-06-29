class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # consider even number of digits and odd number of digits
        return x == reversed_num or x == reversed_num // 10
    
print(Solution.isPalindrome(Solution, 1001))