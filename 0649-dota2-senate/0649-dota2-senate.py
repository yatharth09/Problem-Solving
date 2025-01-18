from collections import defaultdict
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        rq = []
        dq = []
        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)


        while len(rq) != 0 and len(dq) != 0:
            ri = rq[0]
            di = dq[0]

            if ri < di:
                rq.append(ri + n)
            else:
                dq.append(di + n)

            rq.pop(0)
            dq.pop(0)
        
        if len(rq) == 0:
            return "Dire"
        else:
            return "Radiant"
            

        
            



            
       
            
    


        