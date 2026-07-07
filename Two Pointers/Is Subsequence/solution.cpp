class Solution {
public:
    bool isSubsequence(string s, string t) {
        int ans = s.length();
        int cnt = 0;

        for(int x = 0; x < t.length(); ++x)
        {
            if(cnt < ans)
            {
                if(s[cnt] == t[x])
                {
                    cnt += 1;
                }
            }
        }
        return cnt == ans;
    }
};