#include <stack>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> mapping = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            else if (mapping.count(c)) {
                if (st.empty() || st.top() != mapping[c]) {
                    return false;
                }
                st.pop();
            }
        }

        return st.empty();
    }
};