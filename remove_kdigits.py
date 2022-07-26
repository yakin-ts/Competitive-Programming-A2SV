class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack= []
        count = 0
        if len(num)<=k:
            return "0"
        for x in num:
            if not stack:
                stack.append(x)
                continue
            while stack and stack[-1] > x and k > 0:
                stack.pop()
                k-=1
            stack.append(x)
        while k:
            stack.pop()
            k-=1
        return str(int("".join(stack)))