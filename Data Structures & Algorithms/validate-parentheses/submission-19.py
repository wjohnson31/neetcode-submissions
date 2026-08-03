class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}':'{', ')': '(', ']': '['}
        stack = []
        # "([{}])" loop through string
        # add to stack each element not in map ([{ when finding an element in map
        # pop and check if equals 
        for c in s:
            if c not in closeToOpen:
                print(c)
                stack.append(c)
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                    continue
                else:
                    return False
        return not stack