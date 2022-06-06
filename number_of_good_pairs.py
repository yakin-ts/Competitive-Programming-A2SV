class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum(n*(n-1)//2 for n in Counter(nums).values())
    