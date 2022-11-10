class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        res = 1
        l , r = 0,0
        d= {}
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 1 + d.get(s[r], 0)
                r+=1
                res = max(res, r-l)
            else:
                while s[l] is not s[r]:
                    del d[s[l]]
                    l+=1  
                l+=1
                res = max(res, r-l+1)
        return res
                
        
        