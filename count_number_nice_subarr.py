class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        run_sum = 0
        nice = 0
        new_nums = [0 if n%2==0 else 1 for n in nums]
        print(new_nums)
        for i in range(len(new_nums)):
            run_sum+= new_nums[i]
            d = run_sum - k
            nice += freq.get(d,0)
            freq[run_sum] = 1 + freq.get(run_sum,0)
        return nice
