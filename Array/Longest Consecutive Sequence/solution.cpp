class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        sort(nums.begin(), nums.end());
        nums.erase(unique(nums.begin(), nums.end()), nums.end());

        int count = 0;
        int maxLen = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1] + 1) {
                count++;
            } else {
                maxLen = max(maxLen, count);
                count = 0;
            }
        }

        maxLen = max(maxLen, count);

        return maxLen + 1;  
        
    }
};