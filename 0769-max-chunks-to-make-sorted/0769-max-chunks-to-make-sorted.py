class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxx = 0
        count = 0
        for i in range(0, len(arr)):
            if maxx < arr[i]:
                maxx = arr[i]
                
            

            if i == maxx:
                count += 1


            
            
            
        return count

            



        