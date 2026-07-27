class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}':'{',')':'(', ']':'['}
        stack = []
        if len(s) == 1:
            return False
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack and stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
        return not stack