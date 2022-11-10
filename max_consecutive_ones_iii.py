class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        l , r, ans, flip= 0,0,0,0
        for r in range(len(nums)):
            if nums[r]==0:
                flip +=1
            while flip > k:
                if nums[l]==0:
                    flip-=1
                l+=1
            ans = max(ans, r-l+1)

        return ans