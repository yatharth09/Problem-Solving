class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        int n = nums.size();
    for(int i = 0; i < n; i++){
        sum = sum + nums[i];
    }
    if((sum - target) % 2 != 0) return 0;
    if(target > sum) return 0;
    int tar = (sum - target)/2;
    int count = 0;
    int t[n+1][tar+1];
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= tar; j++){
            if(i == 0) t[i][j] = 0; 
            if(j == 0) {
                if(i > 0 and nums[i - 1] == 0) count++;
                t[i][j] = pow(2,count);
                
            }
        }
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= tar; j++){
            if(nums[i-1] <= j)
                t[i][j] = t[i - 1][j - nums[i-1]] + t[i - 1][j];
            else
                t[i][j] = t[i - 1][j];
            
        }
    }

    return t[n][tar];
    }
};