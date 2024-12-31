class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        maxArea = 0
        while low < high:
            maxArea = max((min(height[low], height[high]) * (high - low)), maxArea)
            if(height[low] < height[high]):
                low += 1
            else:
                high -= 1
            
        return maxArea

