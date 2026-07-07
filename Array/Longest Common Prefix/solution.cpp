class Solution {
public:
    string longestCommonPrefix(vector<string>& v) {
        sort(v.begin(), v.end());
        if (v.empty()) 
        {
            return "";
        }

        string str_first = v.front();
        string str_second = v.back();
        string result = "";

        for(int i = 0; i < min(str_first.length(), str_second.length()); ++i)
        {
            if(str_first[i] == str_second[i])
            {
                result += str_first[i];
            }
            else
            {
                break;
            }
        }
        return result;
    }
};