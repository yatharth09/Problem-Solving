class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)

        for edge in edges:
             adj[edge[0]].append(edge[1])
             adj[edge[1]].append(edge[0])
        
        res = 0
        def dfs(curr, parent):
            value = values[curr]

            for child in adj[curr]:
                if child != parent:
                    value += dfs(child, curr)
            
            if value % k == 0:
                nonlocal res
                res += 1

            return value
            


        
        dfs(0, -1)

        return res
        