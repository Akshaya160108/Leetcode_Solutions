class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        s=""
        for x in num:
            s+=str(x)
        n=int(s)
        new=str(n+k)
        num=[]
        for x in new:
            num.append(int(x))
        return num