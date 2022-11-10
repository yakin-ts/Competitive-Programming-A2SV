class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        run_sum = 0
        prefix = {0:1}
        for num in nums:
            run_sum+=num
            d = run_sum - k
            ans += prefix.get(d,0)
            prefix[run_sum] = 1 + prefix.get(run_sum,0)
           
        return ans

'''
[4,3,1,2,2]
sum = 4 , 7 , 9 , 10, 12
sum - k= 0
map = 0:1 , 3:1 , 5:1, 6:1, 8:1
'''
       