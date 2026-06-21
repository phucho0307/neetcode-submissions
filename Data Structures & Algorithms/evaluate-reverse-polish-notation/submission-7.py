import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops ={
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(ops[tokens[i]](b,a))
        return stack[-1]

            

        
        