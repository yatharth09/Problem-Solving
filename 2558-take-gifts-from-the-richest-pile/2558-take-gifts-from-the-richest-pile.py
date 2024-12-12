import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        while k > 0:
            maxx = 0
            for i in range(n):
                if maxx < gifts[i]:
                    maxx = gifts[i]
                    ind = i
            
            leftover = int(maxx ** 0.5)
            gifts[ind] = leftover
            
            k -= 1

        return sum(gifts)
            
        

            
            

                
        
        