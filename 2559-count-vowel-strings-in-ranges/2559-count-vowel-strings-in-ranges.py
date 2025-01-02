class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        temp = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in words:
            if (i[0] in vowels) and (i[-1] in vowels):
                temp.append(1)
            else:
                temp.append(0)
        prefixSum = []
        summ = 0
        for i in temp:
            summ += i
            prefixSum.append(summ)

        print(prefixSum)
        ans = []
        for query in queries:
            if query[0] == 0:
                count = prefixSum[query[1]]
            else:
                count = prefixSum[query[1]] - prefixSum[query[0] - 1]
            ans.append(count)
        
        return ans
