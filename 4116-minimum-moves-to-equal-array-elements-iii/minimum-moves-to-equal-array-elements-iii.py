class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves=0
        maxi=max(nums)
        for x in nums:
            moves+=maxi-x
        return moves