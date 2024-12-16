from heapq import heappop, heappush, heapify
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        size = len(nums)
        minHeap = []
        for i in range(size):
            heappush(minHeap, (nums[i], i))

        
        while k:
            ele, ind = heappop(minHeap)
            ele *= multiplier
            nums[ind] = ele
            heappush(minHeap, (ele, ind))
            k -= 1
        
        return nums


        
        
        