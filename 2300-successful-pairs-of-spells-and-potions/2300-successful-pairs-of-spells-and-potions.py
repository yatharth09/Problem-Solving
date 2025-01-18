class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for spell in spells:
            low = 0
            high = len(potions) - 1
            while low <= high:
                mid = int(low + (high - low)/2)

                if spell * potions[mid] >= success:
                    high = mid - 1
                else:
                    low = mid + 1

            if low < len(potions):
                ans.append(len(potions) - low)
            else:
                ans.append(0)
            
        return ans

        