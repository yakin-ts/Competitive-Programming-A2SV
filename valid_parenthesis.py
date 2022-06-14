class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        for i in range(len(s)):
            if len(stk)==0:
                if s[i]=="(" or s[i]=="{" or s[i]=="[":
                    stk.append(s[i])
                else:
                    return False
            else :
                if stk[-1]=="(":
                    if s[i]==")":
                        stk.pop()
                    elif s[i]=="(" or s[i]=="{" or s[i]=="[":
                        stk.append(s[i])
                    else:
                        return False
                elif stk[-1]=="{":
                    if s[i]=="}":
                        stk.pop()
                    elif s[i]=="(" or s[i]=="{" or s[i]=="[":
                        stk.append(s[i])
                    else:
                        return False
                elif stk[-1]=="[":
                    if s[i]=="]":
                        stk.pop()
                    elif s[i]=="(" or s[i]=="{" or s[i]=="[":
                        stk.append(s[i])
                    else:
                        return False
        return len(stk)==0