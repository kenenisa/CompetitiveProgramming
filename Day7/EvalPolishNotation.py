#this has better time complaxity
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ('+','-','*','/'):
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '/':
                    stack.append(int(a / b))
                elif i == '*':
                    stack.append(a*b)
                elif i == '+':
                    stack.append(a+b)
                else:
                    stack.append(a-b)
            else:
                stack.append(i)
        return stack[0]
# this one had a bad time complexity, trying to improve using stacks
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# while len(tokens) > 1:
#     op = 0
#     for i in range(len(tokens)):
#         if tokens[i] in ('+','-','*','/'):
#             op = i
#             break
#     f,s = op - 2,op - 1
#     value = eval(tokens[f] + tokens[op] + tokens[s])
#     tokens = tokens[:f] + tokens[op:]
#     tokens[f] = str(int(value))    
# print(tokens[0])
    