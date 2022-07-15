class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngre = {x:i for i,x in enumerate(nums1)}
        stack = []
        result = [-1]*len(nums1)
        for i in range(len(nums2)-1,-1,-1):
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if nums2[i] in ngre and stack:
                    result[ngre[nums2[i]]]  = stack[-1]
                stack.append(nums2[i])
        
        return result