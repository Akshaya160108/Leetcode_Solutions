class Solution:
    def reverseByType(self, s: str) -> str:
        lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        letters=[]
        special=[]
        for ch in s:
            if ch in lower:
                letters.append(ch)
            else:
                special.append(ch)
        new=[]
        for ch in s:
            if ch in lower:
                new.append(letters.pop())
            else:
                if len(special)!=0:
                    new.append(special.pop())
        return "".join(new)