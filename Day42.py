strings = ")(){}"
class Solution:
    def isValid(self,stris):
        main_stack = []

        if len(stris) == 1:
            return False
        else:
            open_parenthesis = ['(','[','{']
            for i in stris:
                if i in open_parenthesis:
                    main_stack.append(i)
# Here below else is very very important, like if open brackets is there then append to main stack
# else after appending checking length of the stack.
                else:
                    if len(main_stack) > 0:
                        if i == ')':
                            if main_stack[-1] == open_parenthesis[0]:
                                main_stack.pop()
                            else:
                                return False
                        elif i == ']':
                            if main_stack[-1] == open_parenthesis[1]:
                                main_stack.pop()
                            else:
                                return False
                        elif i == '}':
                            if main_stack[-1] == open_parenthesis[2]:
                                main_stack.pop()
                            else:
                                return False
                    else:
                        return False
        
        return len(main_stack) == 0           
obj = Solution()
print(obj.isValid(strings))

