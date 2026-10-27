class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            # closing, check match
            if c in pair:
                if stack and pair[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # opening, push to stack
            else:
                stack.append(c)

        return len(stack) == 0