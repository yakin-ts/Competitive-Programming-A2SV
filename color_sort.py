class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for n in range(len(nums)-i-1):
                if(nums[n]>nums[n+1]):
                    temp = nums[n]
                    nums[n], nums[n+1] = nums[n+1], temp
        