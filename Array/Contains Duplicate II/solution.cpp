class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        int n =  nums.size();
        for(int idx = 0; idx < n; ++idx)
        {
            int value = nums[idx];
            if((seen.find(value) != seen.end()) && ((idx - seen[value]) <= k))
            {
                return true;
            }
            else
            {
                seen[value] = idx;
            }
        }
        return false;
    }
};