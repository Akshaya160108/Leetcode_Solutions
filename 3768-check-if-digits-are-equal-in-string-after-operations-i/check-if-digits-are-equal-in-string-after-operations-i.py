class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            new=""
            for i in range(len(s)-1):
                n=(int(s[i])+int(s[i+1]))%10
                new+=str(n)
            s=new
        if len(set(s))==1:
            return True
        return False