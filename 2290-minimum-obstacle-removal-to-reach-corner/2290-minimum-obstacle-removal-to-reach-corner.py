import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = float('inf')
        res = []
        pq = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(m):
            row = [inf]*n
            res.append(row)
        heapq.heappush(pq, (0, [ 0, 0]))
        res[0][0] = 0
        while len(pq) > 0:
            curr = heapq.heappop(pq)
            
            distance = curr[0]
            
            i = curr[1][0]
            j = curr[1][1]

            for direction in directions:
                newi = i + direction[0]
                newj = j + direction[1]
                if newi < 0 or newi >= m or newj >= n or newj < 0:
                    continue
                weight = grid[newi][newj]
                if(weight + distance < res[newi][newj]):
                    res[newi][newj] = weight + distance
                    heapq.heappush(pq, (weight + distance, [newi, newj]))

        return res[m-1][n-1]            




        
        