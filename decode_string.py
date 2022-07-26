class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = ''
        counts = ""
        count=0
        for x in s:
            if x is not ']':
                stack.append(x)
            else:
                while stack and stack[-1] is not '[':
                    temp =  stack.pop() + temp
                stack.pop()
                while stack and stack[-1].isnumeric():
                    counts += stack.pop()
                count = int(counts[::-1])
                stack.append(count*temp)
                temp = ''
                counts = ''
        return "".join(stack)
                
                
                
                
            