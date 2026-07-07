class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> result;
        unordered_set<int> target_set(target.begin(), target.end());
        int target_idx = 0;

        for (int i = 1; i <= n; i++) {
            if (target_idx >= target.size()) 
            {
                break;
            }

            result.push_back("Push");

            if (target_set.find(i) == target_set.end()) 
            {
                result.push_back("Pop");
            } 
            else 
            {
                target_idx++;
            }
        }

        return result;
    }
};