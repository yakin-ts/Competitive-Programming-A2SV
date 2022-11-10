class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res =[]
        last = {}
        last_seen = 0
        l=0
        r=0
        for idx in range(len(s)):
            last[s[idx]] = idx
            
        while r < len(s):
            last_seen = max(last_seen,last[s[r]])
            if r== last_seen:
                res.append(r-l+1)
                l = r+1
            r+=1
        return res
    """
    ababcbacadefegdehijhklij
    l       l      l
    
    a - 0  8
    b - 1  5
    """