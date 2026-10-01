class Solution:
    def isValid(self, s: str) -> bool:
        '''arr=['(','{','[',')','}',']']
        valid=True
        for i in range(3):
            if s.count(arr[i])!=s.count(arr[i+3]):
                valid=False
        return valid'''
        stack=[]
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if (ch==')' and top!='(') or (ch==']' and top!='[') or (ch=='}' and top!='{'):
                    return False
        return len(stack)==0