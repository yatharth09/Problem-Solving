from collections import OrderedDict
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sortedDict = OrderedDict()
        size = len(nums)
        low, high = 0, 0
        count = 0

        while high < size:
            if nums[high] not in sortedDict:
                sortedDict[nums[high]] = 1
            else:
                sortedDict[nums[high]] += 1
            
            maxNum, maxFreq = next(iter(sortedDict.items()))
            minNum, minFreq = next(reversed(sortedDict.items()))

            if abs(maxNum - minNum) <= 2:
                count += high - low + 1
                
            else:
                while abs(maxNum - minNum) > 2:
                    if sortedDict[nums[low]] == 1:
                        sortedDict.pop(nums[low])
                    else:
                        sortedDict[nums[low]] -= 1
                    minNum, minFreq = next(iter(sortedDict.items()))
                    maxNum, maxFreq = next(reversed(sortedDict.items()))
                    low += 1
                print(count, high, low, "2nd")
                count += high - low + 1
            
            high += 1

        return count

        

                




        