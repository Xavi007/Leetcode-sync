#include <cstring>

class Solution {
public:
    bool isPalindrome(string s) {

        string rev_s = "";
        for(int i = s.length()-1; i >= 0; --i)
        {
            if(isalnum(s[i]))
            {
                rev_s.push_back(tolower(s[i]));
            }
        }

        string clean_s = "";
        for (int x =rev_s.length()-1; x >= 0; --x)
        {
            clean_s.push_back(rev_s[x]);
        }

        return rev_s == clean_s;
    }
};