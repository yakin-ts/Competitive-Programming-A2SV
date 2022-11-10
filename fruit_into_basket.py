class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r=0,0
        ans =0
        bucket = defaultdict(int)
        while r < len(fruits):
            bucket[fruits[r]] +=1
            while len(bucket) > 2:
                bucket[fruits[l]] -=1
                if bucket[fruits[l]]==0:
                    bucket.pop(fruits[l])
                l+=1
            ans = max(ans, r-l+1)
            r+=1

        return ans
            
        