class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int size_nums = size(nums);
        int max_sum = INT_MIN;
        int current_sum = 0;
        for (int i = 0; i < size_nums; i++)
        {
            current_sum += nums[i];
            max_sum = max(max_sum, current_sum);

            if(current_sum < 0)
            {
                current_sum = 0;
            }
        }
        return max_sum;
    }
};