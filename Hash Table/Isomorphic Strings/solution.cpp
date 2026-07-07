class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char>MapST;
        unordered_map<char, char>MapTS;

        for(int i = 0; i < s.length(); ++i)
        {
            char c1 = s[i], c2 = t[i];

            if(MapST.find(c1) != MapST.end() && MapST[c1] != c2) return false;
            if(MapTS.find(c2) != MapTS.end() && MapTS[c2] != c1) return false;

            MapST[c1] = c2;
            MapTS[c2] = c1;
        }
        return true;
    }
};