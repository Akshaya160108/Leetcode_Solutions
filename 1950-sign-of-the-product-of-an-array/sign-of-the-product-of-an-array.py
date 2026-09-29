class Solution:
    def arraySign(self, nums: list[int]) -> int:
        pro=1
        for x in nums:
            pro*=x
        if pro<0:
            return -1
        elif pro>0:
            return 1
        else:
            return 0