class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        arr=[x for x in str(n)]
        if arr.count(str(x))>=1 and arr[0]!=str(x):
            return True
        return False