class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_nums = [0 for i in nums]
        for x in range(len(nums)):
            for i in range(len(nums)):
                if (nums[x]>nums[i]):
                    count_nums[x] +=1
        return count_nums