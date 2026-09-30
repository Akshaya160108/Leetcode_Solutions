class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        if str(n-1).count('0')==0:
            return [1,n-1]
        else:
            for i in range(2,(n//2)+1):
                if str(n-i).count('0')==0 and str(i).count('0')==0:
                    return [i,n-i]