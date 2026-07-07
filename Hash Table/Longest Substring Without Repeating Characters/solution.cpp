#include<algorithm>
#include <string>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        std::string str_ans = "";

        for(int i = 0; i < s.size(); ++i)
        {
            if(str_ans.find(s[i]) == std::string::npos)
            {
                str_ans += s[i];
            }
            else
            {
                ans = std::max(ans, static_cast<int>(str_ans.size()));
                int dup_ids = str_ans.find(s[i]);
                str_ans = str_ans.substr(dup_ids+1) + s[i];
            }
        }

        ans = std::max(ans, static_cast<int>(str_ans.size()));
        return ans;
    }
};