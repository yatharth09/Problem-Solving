from typing import List, Dict, Tuple 
class Solution: 
        
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int: 
        MOD = 10**9 + 7
        dp = [0] * (high + 1) 
        dp[0] = 1 # Base case: there's one way to form an empty string 
        for length in range(1, high + 1): 
            if length >= zero: 
                dp[length] += dp[length - zero] % MOD
            if length >= one: 
                dp[length] += dp[length - one] %MOD# Sum up the counts for lengths in the range [low, high] 
        
        return sum(dp[low:high + 1]) %MOD