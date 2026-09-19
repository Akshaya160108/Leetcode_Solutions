class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        arr1=startTime.split(":")
        startseconds=int(arr1[0])*3600+int(arr1[1])*60+int(arr1[2])
        arr2=endTime.split(":")
        endseconds=int(arr2[0])*3600+int(arr2[1])*60+int(arr2[2])
        return abs(startseconds-endseconds)