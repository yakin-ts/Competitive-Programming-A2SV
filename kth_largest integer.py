class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_int = [int(x) for x in nums]
        nums_int.sort()
        return str(nums_int[-k])