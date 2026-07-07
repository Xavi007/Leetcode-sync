class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.size()-1, j = b.size()-1, c = 0;
        string res;
        while (i >= 0|| j >= 0 || c )
        {
            int sum = c;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            res.push_back((sum & 1) + '0');
            c = sum >> 1;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};