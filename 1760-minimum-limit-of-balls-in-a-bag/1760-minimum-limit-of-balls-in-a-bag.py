class Solution:
    def isValid(self, mid: int, nums: List[int], n: int) -> bool:
        for i in nums:
            n -= int(i/mid)
            if i % mid == 0:
                n += 1
        if n >= 0:
            return True
        return False



    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low = 1
        high = max(nums)
        ans = -1
        while low <= high:
            mid = int(low + (high - low)/2)
            if self.isValid(mid, nums, maxOperations):
                ans = int(mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans
                
        