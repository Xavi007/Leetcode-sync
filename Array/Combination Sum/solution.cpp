class Solution {
public:
    set<vector<int>> s;
    void helper(vector<int>& arr, int idx, int target, vector<vector<int>> &ans, vector<int> &comb)
    {

        if(idx == arr.size() || target < 0)
        {
            return;
        }

        
        if(target == 0)
        {
            if(s.find(comb) == s.end())
            {
                ans.push_back(comb);
                s.insert(comb);
                return;
            }
        }

        comb.push_back(arr[idx]);


        helper(arr, idx+1, target-arr[idx], ans, comb);

        helper(arr, idx, target-arr[idx], ans, comb);

        comb.pop_back();

        helper(arr, idx+1, target, ans, comb);

    }


    vector<vector<int>> combinationSum(vector<int>& arr, int target) {
        vector<vector<int>> ans;
        vector<int> comb;

        helper(arr, 0, target, ans, comb);

        return ans;
    }
};