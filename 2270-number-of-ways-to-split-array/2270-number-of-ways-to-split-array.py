class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalsumm = sum(nums)
        k = totalsumm/2
        summ = 0
        count = 0
        for i in range(len(nums) - 1):
            summ += nums[i]
            if summ >= k:
                count += 1

        return count  



        