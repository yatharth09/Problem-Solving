class Solution {
public:
    bool valid(int mid, vector<int>&nums, int n)
    {
        for(auto i: nums){
            n-= i/mid;
            if(i % mid == 0) n++;
        }
        if(n>=0) return true;
        return false;
    }
    int minimumSize(vector<int>& nums, int maxOperations) {
        
         
        int start = 1;
        int end = *max_element(nums.begin(),nums.end());
        int ans = -1;
        while(start <= end)
        {
            int mid = start + (end - start)/2;
            if(valid(mid, nums, maxOperations))
            {
                ans = mid;
                end = mid - 1;
            }
            else
                start = mid + 1;
            
            
        }
        return ans;
    }
};