class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "[": "]", "{": "}"} # opens -> closes
        stack = []

        for c in s:
            if c in pairs: # if an opening bracket
                stack.append(pairs[c]) # add corresponding closing
            elif not stack or stack.pop() != c:
                return False # closing bracket and does not match expected
        
        return not stack