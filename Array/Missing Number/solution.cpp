class Solution {
public:
    int missingNumber(vector<int>& nums) {
    int n = nums.size();

    int total_sum = (n * (n+1)) / 2;

    long long arr_sum = 0;
    for (int x : nums) arr_sum += x;

    return total_sum - arr_sum;
    }
};