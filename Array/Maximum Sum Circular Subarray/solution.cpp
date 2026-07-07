class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int total = 0;
        int max_sum = nums[0], min_sum = nums[0];
        int curr_max = 0, curr_min = 0;

        for (int x : nums) {
            curr_max = max(x, curr_max + x);
            max_sum = max(max_sum, curr_max);

            curr_min = min(x, curr_min + x);
            min_sum = min(min_sum, curr_min);

            total += x;
        }

        return max_sum < 0 ? max_sum : max(max_sum, total - min_sum);
    }
};