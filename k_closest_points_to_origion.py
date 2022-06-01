class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        for i in range(len(points)):
            dic[i] = (points[i][0])**2 + (points[i][1])**2
        result = {key:val  for key, val in sorted(dic.items(), key = lambda ele: ele[1],)}
        points = [points[key] for key in result.keys()]
        return points[:k]
        
        
        
        

                