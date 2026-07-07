class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        unordered_map<char, string> mp = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
            {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
            {'8', "tuv"}, {'9', "wxyz"}
        };

        vector<string> ans;

        function<void(int, string)> helper = [&](int i, string cur) {
            if (i == digits.size()) {
                ans.push_back(cur);
                return;
            }

            for (char c : mp[digits[i]]) {
                helper(i + 1, cur + c);
            }
        };

        helper(0, "");
        return ans;
    }
};