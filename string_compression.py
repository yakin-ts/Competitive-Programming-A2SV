class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        l=0
        r=0
        while r < len(chars):
            if chars[l] is chars[r]:
                count+=1
                if r==len(chars)-1:
                    if count > 1:
                        temp = str(count)
                        l+=1
                        for d in temp:
                            chars[l] = d
                            l+=1
                    else:
                        l+=1
                         
                r+=1
            else:
                if count > 1:
                    temp = str(count)
                    l+=1
                    for d in temp:
                        chars[l] = d
                        l+=1
                    chars[l] = chars[r]
                else:
                    l+=1
                    chars[l]=chars[r]
                count = 0
        return l