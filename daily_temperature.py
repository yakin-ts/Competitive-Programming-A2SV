class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        waitDays = [0]*len(temp)
        stack = []
        for i, item in enumerate(temp):
            if not stack:
                    stack.append(i)
            else:
                    while stack and temp[stack[-1]] < item:
                        idx = stack.pop()
                        waitDays[idx] = i - idx
                    stack.append(i)
        return waitDays
    
      
        
        