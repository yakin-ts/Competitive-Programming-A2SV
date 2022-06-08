class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ptr_r = len(nums)-1
        ptr_l = 0
        op_count = 0
        nums.sort()
        while ptr_l < ptr_r:
            if nums[ptr_l] + nums[ptr_r] == k:
                ptr_r -=1
                ptr_l +=1
                op_count +=1
            elif nums[ptr_l] + nums[ptr_r] > k:
                ptr_r -=1
            else:
                ptr_l +=1
        return op_count
        
            