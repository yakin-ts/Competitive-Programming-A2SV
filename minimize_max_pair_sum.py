class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_pair = [0]*(len(nums)//2)
        count = 0
        rev_count = len(nums)-1
        while count < rev_count:
            min_pair[count] += (nums[count]+nums[rev_count])
            count +=1
            rev_count -=1
        return max(min_pair)
        
        