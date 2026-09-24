class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans=[]
        s=[]
        def fun(i):
            if i==len(digits):
                ans.append("".join(s))
                return
            for ch in d[digits[i]]:
                s.append(ch)
                fun(i+1)
                s.pop()
        fun(0)
        return ans