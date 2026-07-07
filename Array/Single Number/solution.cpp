class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;

        if(nums.size() > 1)
        {
            for(int val : nums)
            {
                ans ^= val;
            }
            return ans;
        }
        else
        {
            return nums[0];
        }
    }
};