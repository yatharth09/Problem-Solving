class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxx = max(candies)
        for i in candies:
            if (i +  extraCandies) >= maxx:
                res.append(True)
            else:
                res.append(False)

        return res
        