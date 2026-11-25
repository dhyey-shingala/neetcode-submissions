class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or s is None or s[0] in ('}', ')', ']'):
            return False

        stack = []

        for i in range(len(s)):
            if s[i] in ('{', '(', '['):
                stack.append(s[i])
            elif s[i] == '}' and len(stack) != 0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']' and len(stack) != 0:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == ')' and len(stack) != 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False