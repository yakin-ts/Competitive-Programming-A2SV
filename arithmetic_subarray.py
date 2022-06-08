class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        sub_arr_status = []
        for i in range(len(l)):
            pool = sorted(nums[l[i]:r[i]+1])
            print(pool)
            if len(pool)<2:
                sub_arr_status.append(False)
            elif len(pool)==2:
                sub_arr_status.append(True)
            else:
                d = pool[1]-pool[0]
                ct_art = True
                for j in range(len(pool)):
                    if pool[j] != pool[0] + d*j:
                        ct_art = False
                        break
                if ct_art==True:
                    sub_arr_status.append(True)
                else:
                    sub_arr_status.append(False)
        return sub_arr_status