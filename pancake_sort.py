class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i!=0 and arr[i-1] > arr[i]:
                break
            else:
                if i==len(arr)-1:
                    return []
        start=max(arr)
        trav = 0
        ans = []
        while start != 0:
            if arr[trav] == start:
                self.flip(trav,arr)
                ans.append(trav+1)
                self.flip(start-1,arr)
                ans.append(start)
                start -=1
                trav = 0
            else:
                trav +=1
        return ans
    
    def flip(self,end: int,arr: List[int]) -> List[int]:
        start = 0
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            end -=1
            start +=1
        return arr
    
    
#     NOT QUITE PANCAKE SORT BUT  IT SORTS  ALRIGHT >>>

# def pancakeSort(self, arr: List[int]) -> List[int]:
#         for i in range(len(arr)):
#             if i!=0 and arr[i-1] > arr[i]:
#                 break
#             else:
#                 if i==len(arr)-1:
#                     return []
#         # bound = 0
#         start=0
#         trav = 1
#         while start != len(arr):
#             if arr[trav]-1 == start:
#                 self.reverse(start,trav,arr)
#                 start +=1
#                 trav = start
#             else:
#                 trav +=1
#         return arr
    
#     def reverse(self,start: int,end: int,arr: List[int]) -> List[int]:
#         while start< end:
#             temp = arr[start]
#             arr[start] = arr[end]
#             arr[end] = temp
#             start +=1
#             end -=1
#         return arr