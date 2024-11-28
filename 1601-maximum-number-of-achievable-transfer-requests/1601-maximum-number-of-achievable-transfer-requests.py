class Solution:
    def solve(self, idx, res, build, m, requests, count):
        if idx == m:
            isValid = True
            for i in build:
                if i == 0:
                    continue
                else:
                    isValid = False
                    break

            if(isValid):
                res[0] = max(res[0], count[0])

            return
        
        fr = requests[idx][0]
        to = requests[idx][1]

        build[fr] -= 1
        build[to] += 1
        count[0] += 1
        self.solve(idx + 1, res, build, m, requests, count)
        count[0] -= 1
        build[fr] += 1
        build[to] -= 1
        self.solve(idx + 1, res, build, m, requests, count)

        return


    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = [0]
        build = [0] * n
        count = [0]
        m = len(requests)
        self.solve(0, res, build, m, requests, count)

        return res[0]


        