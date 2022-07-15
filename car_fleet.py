class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival = [float(target - p)/s for p,s in sorted(zip(position,speed))]
        mono_stack = []
        for item in arrival:
            while mono_stack and mono_stack[-1] <= item:
                mono_stack.pop()
            mono_stack.append(item)
        return len(mono_stack)
            