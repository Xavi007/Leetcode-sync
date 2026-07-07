class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hp;

        for(int i = 0; i < nums.size(); ++i)
        {
            if(hp.count(target-nums[i]))
            {
                return {hp[target-nums[i]], i};
            }
            hp[nums[i]] = i;
        }
        return {};
    }
};