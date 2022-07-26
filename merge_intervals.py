class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        new_interval = sorted(intervals, key=lambda x: x[0])
        print(new_interval)
        start = new_interval[0][0]
        end = new_interval[0][1]
        for i in range(1,len(intervals)):
            if new_interval[i][0]<=end:
                end = max(end, new_interval[i][1])
            else:
                ans.append([start,end])
                start = new_interval[i][0]
                end = new_interval[i][1]
        ans.append([start,end])
        return ans