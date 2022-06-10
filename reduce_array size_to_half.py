class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = Counter(arr)
        dic_x = sorted(dic.items(), key=operator.itemgetter(1))
        sortdict = dict(dic_x)
        freq_arr = [freq for freq in sortdict.values()]
        target = len(arr)//2
        if max(freq_arr) >= target:
            return 1
        freq =0
        sets = 0
        start = len(freq_arr)-1
        while freq < target:
            freq += freq_arr[start]
            start -=1
            sets +=1
        return sets
            
# 1. hash table for keeping the frequency of duplicate
# 2. sort the hash table and create frequency array/list from it
# 3. start comparing the target from the highest frequency
# 4. sum the frequencies until  they meet the target/minimum
            
            
        
        