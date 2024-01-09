class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        isPalindrome check if a number is palindrome number or not
        :param x:
        :return:
        """
        if x < 0:
            return False
        else:
            lst = list()
            while x != 0:
                r = x % 10
                lst.append(r)
                x = x // 10

            l = len(lst) - 1
            i = 0
            while i <= l:
                if lst[i] != lst[l]:
                    return False
                i += 1
                l -= 1
            return True

    def isPalindromeOptimized(self, x: int) -> bool:
        """
        Optimised approach:
        x= 121 rev=0
        x=x//10 rev = rev + x%10 , condition : while x > rev
        x = 12 , rev = 1  True
        x = 1  , rev = 12 False
        Now check x==rev or x == rev//10
        """

        # handle for neg numbers and ending with 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev_half = 0
        while x > rev_half:
            rev_half = rev_half * 10 + x % 10
            x //= 10

        return x == rev_half or x == rev_half // 10

    def isPalindromeUsingList(self, x: int) -> bool:
        lst = list(str(x))
        rev = lst.copy()
        rev.reverse()
        return lst == rev

    def isPalindromeBest(self, x: int) -> bool:
        if x >= 0:
            if x == int((str(x))[::-1]):
                return True
        return False


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))

print(s.isPalindromeUsingList(121))
print(s.isPalindromeUsingList(-121))
print(s.isPalindromeUsingList(1221))
