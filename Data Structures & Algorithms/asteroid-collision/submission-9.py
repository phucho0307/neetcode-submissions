class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for r in asteroids:
            stack.append(r)
            while len(stack)>1 and stack[-1]<0 and stack[-2]>0:
                if abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1]) > abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                    stack.append(r)
                else:
                    stack.pop()

        return stack
