class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key = lambda x:x[0])
        n = len(intervals)
        i = 0
        count = 0
        j = 1
        while j < n:
            if intervals[i][1] <= intervals[j][0]:
                i = j
                j += 1
            elif intervals[i][1] < intervals[j][1]:
                count += 1
                j += 1
            else:
                count += 1
                i = j
                j += 1
        
        return count
        