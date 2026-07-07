class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> seen;

        if(s.length() != t.length())
        {
            return false;
        }

        for(int i = 0; i < s.length(); ++i)
        {
            if(seen.find(s[i]) != seen.end())
            {
                seen[s[i]] += 1;
            }
            else
            {
                seen[s[i]] = 1;
            }
        }

        for(int x = 0; x < t.length(); ++x)
        {
            if(seen.find(t[x]) != seen.end())
            {
                seen[t[x]] -= 1;
                if(seen[t[x]] < 0)
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};