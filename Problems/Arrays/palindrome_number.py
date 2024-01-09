class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            lst = list()
            while x!=0:
                r = x%10
                lst.append(r)
                x = x//10

            l = len(lst)-1
            i = 0
            while (i<=l):
                if lst[i]!=lst[l]:
                    return False
                i+=1
                l-=1
            return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
