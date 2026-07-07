#include <iostream>
#include <string>
#include <cctype>

using namespace std;

class Solution {
public:
    bool isValid(const string& word) {
        string vowels = "aeiouAEIOU";
        int vo_count = 0;
        int con_count = 0;
        int al_num = 0;

        for (char ch : word) 
        {
            if (!isalnum(ch)) 
            {
                return false;
            }
            if (isdigit(ch)) 
            {
                al_num++;
            } 
            else if (isalpha(ch)) 
            {
                if (vowels.find(ch) != string::npos) 
                {
                    vo_count++;
                } 
                else 
                {
                    con_count++;
                }
            }
        }

        int total_count = vo_count + con_count + al_num;
        return (vo_count >= 1 && con_count >= 1 && total_count >= 3);
    }
};
