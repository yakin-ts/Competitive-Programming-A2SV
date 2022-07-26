class Solution:
    def absDiff(self,arr,max_lst, min_lst):
        return arr[max_lst[0]] - arr[min_lst[0]]
        
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        keep_max = deque([0])
        keep_min = deque([0])
        l = 0
        r = 1
        run_count = 1
        max_count = 1
        while r < len(nums) and l <= r:
            if nums[r] < nums[keep_min[-1]]:
                while keep_min and nums[keep_min[-1]] > nums[r]:
                    keep_min.pop()
            elif nums[r] > nums[keep_max[-1]]:
                while keep_max and nums[keep_max[-1]] < nums[r]:
                    keep_max.pop()
            keep_max.append(r)
            keep_min.append(r)
            while self.absDiff(nums,keep_max,keep_min) > limit:
                l+=1
                run_count -=1
                if l > keep_max[0]:
                    keep_max.popleft()
                if l > keep_min[0]:
                    keep_min.popleft()
            max_count = max(max_count, run_count+1)
            r +=1
            run_count +=1
        return max_count