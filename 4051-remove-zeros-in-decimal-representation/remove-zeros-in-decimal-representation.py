class Solution:
    def removeZeros(self, n: int) -> int:
        arr=[x for x in str(n)]
        while '0' in arr:
            arr.remove('0')
        return int("".join(arr))