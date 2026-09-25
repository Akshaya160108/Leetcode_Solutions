class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year=int(date[0:4])
        month=int(date[5:7])
        day=int(date[8:10])
        res=""
        res+=bin(year)[2:]
        res+="-"
        res+=bin(month)[2:]
        res+="-"
        res+=bin(day)[2:]
        return res