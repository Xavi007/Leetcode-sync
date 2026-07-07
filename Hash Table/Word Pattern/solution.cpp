class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        string word;
        stringstream ss(s);

        while (ss >> word)
            words.push_back(word);

        if (words.size() != pattern.length())
            return false;

        unordered_map<char, string> mapPattern;
        unordered_map<string, char> mapWord;        

        for(int i =0; i < pattern.length(); ++i)
        {
            char c1 = pattern[i];
            string c2 = words[i];
            if (mapPattern.find(c1) !=  mapPattern.end() && mapPattern[c1] != c2) return false;
            if (mapWord.find(c2) != mapWord.end() && mapWord[c2] != c1) return false;

            mapPattern[c1] = c2;
            mapWord[c2] = c1;
        }
        return true;
    }
};