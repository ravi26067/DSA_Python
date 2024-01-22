class Solution:
    def isValid(self, s: str) -> bool:
        res = False
        k = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                k.append(s[i])
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(k)==0:
                    res=False
                    return res

                r = k[-1]
                if (r == '(' and s[i] == ')') or (r == '[' and s[i] == ']') or (r == '{' and s[i] == '}'):
                    k.pop()
                else:
                    res = False
                    break
        if len(k) != 0:
            return False
        return True
