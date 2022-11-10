class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = 0
        r= len(people)-1

        while r >l:
            if people[r] is limit:
                boats+=1
                r-=1
            if r > l and people[r] + people[l] <= limit:
                l+=1
                r-=1
                boats+=1
            if r>l and people[r] + people[l] > limit:
                r-=1
                boats+=1
            if r==l:
                boats+=1
                r-=1    
        return boats
                    
'''
[1 2 2 3 ]
[1 3 5 8]
(1,2), (3), (2)
[ 3 3 4 5]
[ 3 6 10 15]

'''