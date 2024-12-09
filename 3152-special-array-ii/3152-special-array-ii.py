class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefixSum = [1] * n
        count = 1
        ans = []
        for i in range(1, n):
            if (nums[i - 1] % 2 == 0 and nums[i] % 2 == 0) or (nums[i - 1] % 2 != 0 and nums[i] % 2 != 0 ):
                count = 1
                continue
            else:
                count += 1
                prefixSum[i] = count
        

        for i in queries:
            if i[1] - i[0] < prefixSum[i[1]]:
                ans.append(True)
            else:
                ans.append(False)

        return ans



            


        