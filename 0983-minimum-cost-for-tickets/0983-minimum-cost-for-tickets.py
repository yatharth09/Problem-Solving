class Solution:
    def solve(self, days, costs, ind, memo):
        # If we have processed all days, no additional cost is required
        if ind >= len(days):
            return 0
        
        # If already computed, return the stored result
        if ind in memo:
            return memo[ind]

        # Calculate costs for all three pass options
        # 30-day pass
        payedTill = days[ind] + 29
        newInd = ind
        while newInd < len(days) and days[newInd] <= payedTill:
            newInd += 1
        cost30 = costs[2] + self.solve(days, costs, newInd, memo)
        
        # 7-day pass
        payedTill = days[ind] + 6
        newInd = ind
        while newInd < len(days) and days[newInd] <= payedTill:
            newInd += 1
        cost7 = costs[1] + self.solve(days, costs, newInd, memo)
        
        # 1-day pass
        cost1 = costs[0] + self.solve(days, costs, ind + 1, memo)
        
        # Store the minimum cost in memo and return it
        memo[ind] = min(cost30, cost7, cost1)
        return memo[ind]

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        memo = {}
        return self.solve(days, costs, 0, memo)
