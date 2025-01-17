class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = 0
        alt = []
        for i in gain:
            prefixSum += i
            alt.append(prefixSum)
        
        return max(max(alt), 0)
        