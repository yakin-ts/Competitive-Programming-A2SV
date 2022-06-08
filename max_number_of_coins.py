class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coin = 0
        for x in range(len(piles)//3,len(piles),2):
            max_coin += piles[x] 
        return max_coin