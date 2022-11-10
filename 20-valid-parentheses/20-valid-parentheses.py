class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            ch = s[i]
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if ch==')':
                    if '(' != stack.pop():
                        return False
                elif ch =='}':
                    if '{'!=stack.pop():
                        return False
                else:
                    if '['!=stack.pop():
                        return False
            
        if len(stack)!=0:
            return False
        return True