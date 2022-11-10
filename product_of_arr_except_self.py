class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        output = [1]*len(nums)
        tp = 1
        for i in range(len(nums)):
            if i is 0:
                left[i]=tp
                tp*=nums[i]
            else:
                left[i]=tp
                tp*=nums[i]
        tp=1
        for j in range(len(nums)-1,-1,-1):
            print(j)
            if j == len(nums)-1:
                right[j]=tp
                tp*=nums[j]
            else:
                right[j]=tp
                tp*=nums[j]
        print(left ,right)
        for i in range(len(nums)):
            output[i]=left[i]*right[i]
        return output

        