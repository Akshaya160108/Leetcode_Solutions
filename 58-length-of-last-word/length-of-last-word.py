class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        #return l
        return len(l[-1])