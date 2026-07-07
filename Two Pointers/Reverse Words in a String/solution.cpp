class Solution {
public:
    string reverseWords(string s) 
    {
        string result;
        int i = s.length() - 1;
        
        while (i >= 0) 
        {
            while (i >= 0 && s[i] == ' ') i--;
            
            int j = i;
            
            while (i >= 0 && s[i] != ' ') i--;
            
            if (j >= 0) {
                if (!result.empty()) result += " ";
                result += s.substr(i + 1, j - i);
            }
        }
        
        return result;
    }
};