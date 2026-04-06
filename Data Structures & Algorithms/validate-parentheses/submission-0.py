class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p1 in s:
            if p1 in '({[':
                stack.append(p1)
            else:
                if not stack:
                    return False
                p2 = stack.pop()
                if p1 == ')' and p2 != '(':
                    return False
                if p1 == '}' and p2 != '{':
                    return False
                if p1 == ']' and p2 != '[':
                    return False
        return not stack