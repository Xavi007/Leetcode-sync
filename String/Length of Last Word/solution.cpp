class Solution {
public:
    int lengthOfLastWord(string s) {
        int cnt = 0;

        for(int x = s.size()-1; x >= 0; x--)
        {
            if (s[x] == ' ')
            {
                if(cnt != 0)
                {
                    return cnt;
                }
            }
            else
            {
                cnt++;
            }
        }
        return cnt;
    }
};