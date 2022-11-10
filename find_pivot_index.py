class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leng = len(nums)
        left = nums.copy()
        right = nums.copy()
        for i in range(1,leng):
            left[i] = left[i] + left[i-1]
            right[leng-1-i] = right[leng-1-i] + right[leng-i]
        for i in range(len(left)):
            if left[i]==right[i]:
                return i
        return -1 



"""
1 8 11 17 22 28
28 27 20 17 11 6
"""