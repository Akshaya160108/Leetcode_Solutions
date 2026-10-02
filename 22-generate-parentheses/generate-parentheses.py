def generate(i,ans,string,opencount,closecount,n):
    if opencount==n and closecount==n:
        ans.append("".join(string))
        return
    if opencount<n:
        string.append('(')
        generate(i+1,ans,string,opencount+1,closecount,n)
        string.pop()
    if opencount>closecount:
        string.append(')')
        generate(i+1,ans,string,opencount,closecount+1,n)
        string.pop()
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        string=[]
        opencount=0
        closecount=0
        generate(0,ans,string,opencount,closecount,n)
        return ans