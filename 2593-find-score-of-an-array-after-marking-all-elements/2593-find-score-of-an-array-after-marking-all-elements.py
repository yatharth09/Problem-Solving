
class Solution:
    def findScore(self, nums: List[int]) -> int:
        maxHeap = []
        score = 0
        size = len(nums)
        visited = [False] * size
        flag = True
        count = 0
        while count < size:
            minEle = float('inf')
            ind = 0
            for i in range(size):
                if minEle > nums[i] and visited[i] == False:
                    minEle = nums[i]
                    ind = i
            score += minEle
            visited[ind] = True
            count += 1
            if ind + 1 < size and visited[ind + 1] == False:
                visited[ind + 1] = True
                count += 1
            if ind - 1 >= 0 and visited[ind - 1] == False: 
                visited[ind - 1] = True
                count += 1

            

            

        return score
                
            
                

                
            

        