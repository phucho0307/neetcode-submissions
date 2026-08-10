class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for i in range (len(operations)):
            op = operations[i]
            if op.lstrip('-').isdigit():
                stack.append(op)
                res += int(stack[-1])
            elif op == "D" and stack:
                cur = int(stack[-1])*2
                stack.append(str(cur))
                res += int(stack[-1])
            elif op == "+" and len(stack)>1:
                cur = int(stack[-1]) + int(stack[-2])
                stack.append(str(cur))
                res += int(stack[-1])
            elif op == "C" and stack:
                cur = stack.pop()
                res -= int(cur)
        return res

