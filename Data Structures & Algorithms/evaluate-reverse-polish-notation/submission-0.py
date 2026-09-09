class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()

                if token == "+":
                    stack.append(int(x) + int(y))
                elif token == "-":
                    stack.append(int(x) - int(y))
                elif token == "*":
                    stack.append(int(x) * int(y))
                else:
                    stack.append(int(int(x) / int(y)))

            else:
                stack.append(int(token))

        return stack.pop()