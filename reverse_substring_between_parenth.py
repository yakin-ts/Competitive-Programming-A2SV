class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for item in s:
            if item!=")":
                stack.append(item)
            else:
                rev = []
                x = stack.pop()
                while x !="(":
                    rev.append(x)
                    x = stack.pop()
                while len(rev) > 0:
                    stack.append(rev.pop(0))
        result = "".join(stack)
        return result
            