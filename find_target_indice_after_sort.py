class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(len(nums)-x-1):
                if (nums[y]>nums[y + 1]):
                    temp = nums[y]
                    nums[y],nums[y+1] =nums[y+1] ,temp
        target_counts = []
        for i in range(len(nums)):
            if (target == nums[i]):
                target_counts.append(i)
        return target_counts