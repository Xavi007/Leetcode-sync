class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> mp;

        for (char c : t) {
            mp[c]++;
        }

        int cnt = t.size();
        int l = 0;

        int minLen = INT_MAX;
        int startIndex = -1;

        for (int r = 0; r < s.size(); r++) {
            if (mp[s[r]] > 0) {
                cnt--;
            }

            mp[s[r]]--;

            while (cnt == 0) {
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    startIndex = l;
                }

                mp[s[l]]++;

                if (mp[s[l]] > 0) {
                    cnt++;
                }

                l++;
            }
        }

        return startIndex == -1 ? "" : s.substr(startIndex, minLen);
    }
};