class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        prev = 0
        for i in range(0, len(flowerbed) - 1):
            if prev == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
            prev = flowerbed[i]
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1
            if n == 0:
                return True
        return False

            
        