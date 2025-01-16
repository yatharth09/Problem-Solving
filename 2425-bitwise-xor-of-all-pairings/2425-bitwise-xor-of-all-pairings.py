from collections import defaultdict
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        mp = defaultdict(lambda: 0)
        len2 = len(nums2)
        len1 = len(nums1)
        for i in nums1:
            mp[i] += len2
        
        for j in nums2:
            mp[j] += len1
        
        ans = 0
        for key, value in mp.items():
            if value % 2 != 0:
                ans = ans ^ key


        return ans

        