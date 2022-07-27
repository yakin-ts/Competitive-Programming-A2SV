class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pp = 0
        ps = 0
        while ps<len(pushed) and pp<len(popped):
            if not stack:
                stack.append(pushed[ps])
                ps+=1
            while stack and stack[-1]!=popped[pp]:
                if ps>=len(pushed):
                    break
                else:
                    stack.append(pushed[ps])
                    ps+=1    
            while stack and stack[-1]==popped[pp]:
                stack.pop()
                pp+=1
        if ps>=len(pushed):
            while stack and stack[-1]==popped[pp]:
                stack.pop()
            if not stack:
                return True
            elif stack and stack[-1]!=popped[pp]:
                return False
        