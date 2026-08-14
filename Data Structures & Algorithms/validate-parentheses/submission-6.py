class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        elif s[0] == ']' or s[0] == ')' or s[0] == '}':
            return False
        



        stack = []



        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False

        if not stack:
            return True
        else:
            return False


        