class Solution {
public:
    bool isPalindrome(string &s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right])
                return false;
            left++;
            right--;
        }
        return true;
    }

    string longestPalindrome(string s) {
        int n = s.length();

        for (int len = n; len >= 1; len--) {
            for (int start = 0; start <= n - len; start++) {
                if (isPalindrome(s, start, start + len - 1)) {
                    return s.substr(start, len);
                }
            }
        }

        return "";
    }
};