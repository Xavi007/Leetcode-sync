class Solution {
public:
    int helper(vector<int>& nums, int start, int end)
    {
        int n = nums.size();

        int prev1 = nums[start];
        int prev2 = max(nums[start], nums[start+1]);
        int result = prev2;

        for(int i = start + 2, j = 2; i <= end; ++i, ++j)
        {
            result = max(prev2, prev1 + nums[i]);

            prev1 = prev2;
            prev2 = result;
        }

        return result;
    }

    int rob(vector<int>& nums) 
    {
        if(nums.size() == 1) return nums[0];
        if(nums.size() == 2) return max(nums[0], nums[1]);

        return max(helper(nums, 0, nums.size()-2), helper(nums, 1, nums.size()-1));
    }
};