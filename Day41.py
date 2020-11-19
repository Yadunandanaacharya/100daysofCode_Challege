# #  Valid Parentheses
# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true

stringis = "){"
class Solution:
    def isValid(self, s):
        main_stack = []
        
        if len(s) == 1:
            return False
        else:
            open_parathesis = ['(','{','[']
            for i in s:
                if i in open_parathesis:
                    main_stack.append(i)
                if len(s) >= 0:
                    
                    if i == ')':
                        if main_stack[-1] == open_parathesis[0]:
                            main_stack.pop()
                        else:
                            return False
                
                    elif i == '}':
                        if main_stack[-1] == open_parathesis[1]:
                            main_stack.pop()
                        else:
                            return False
                
                    elif i == ']':
                        if main_stack[-1] == open_parathesis[2]:
                            main_stack.pop()
                        else:
                            return False
                else:
                    return False
        return len(main_stack) == 0

ob = Solution()
print(ob.isValid(stringis))