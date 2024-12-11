class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        size = len(nums)
        ranNums = []
        for i in range(size):
            ran = [nums[i] - k, nums[i] + k]
            ranNums.append(ran)
        # This question has been converted to finding out the maximum overlapping interval 
        ranNums = sorted(ranNums, key=lambda x: x[0])
        group = []
        count = 1
        print(ranNums)
        ans = 1
        i = 0
        while i < size:
            cs = ranNums[i][0]
            ce = ranNums[i][1]
            
            if len(group) > 0:
                fs = group[0][0]
                fe = group[0][1]
            

            if len(group) and cs <= fe:
                group.append(ranNums[i])
                ans = max(ans, len(group))
            else:
                if len(group) > 0:
                    group.pop(0)
                group.append(ranNums[i])

            i += 1
        
        return ans

        
            



        