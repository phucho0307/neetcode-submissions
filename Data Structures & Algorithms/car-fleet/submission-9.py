class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = list(zip(position, speed))
        stack  = []
        for p, s in reversed(sorted(car)):
            t = (target-p)/s
            if stack and stack[-1]>= t: continue
            else: stack.append(t)

        return len(stack)
        