class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        count = 0
        l=0
        r=len(tokens)-1
        while r>=l:
            if tokens[l] <= power:
                count+=1
                score = max(score, count )
                power -= tokens[l]
                l+=1
            elif tokens[r] <= power:
                count+=1
                score = max(score, count)
                power -= tokens[r]
                r-=1
            elif score >= 1:
                count-=1
                score = max(score, count)
                power += tokens[r]
                r-=1
            else:
                l+=1
        return score

        
        '''
        score = 0
        power = x
        tokens= [x,y,z]
        goal = maximize score
        rule:
        1- if power >= token[i] => power - tokens[i] & score += 1 
        2- if score >= 1 => power + tokens[i] & score-=1

        example : [100,200,300,400]
                        l    r
        power = 100
        score = 0

        '''