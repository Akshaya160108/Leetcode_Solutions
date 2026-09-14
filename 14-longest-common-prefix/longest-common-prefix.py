class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        ans=""
        for i in range(min(len(v[0]),len(v[-1]))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans