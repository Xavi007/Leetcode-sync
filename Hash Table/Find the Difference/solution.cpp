class Solution {
public:
    char findTheDifference(string s, string t) {
        int total_val = 0;
        for(int i = 0; i < t.size(); i++)
        {
            total_val += (int)t[i];
        }

        for(int x = 0; x < s.size(); x++)
        {
            total_val -= (int)s[x];
        }

        return (char)total_val;
    }
};