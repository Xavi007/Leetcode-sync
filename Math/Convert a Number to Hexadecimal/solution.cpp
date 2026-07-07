class Solution {
public:
    string toHex(int num) {
        if(num == 0)
        {
            return "0";
        }
        
        uint32_t n = static_cast<uint32_t>(num);

        string digits = "0123456789abcdef";
        string res;

        while (n != 0) 
        {
            res.push_back(digits[n & 0xF]); 
            n >>= 4;                       
        }

        reverse(res.begin(), res.end());
        return res;

    }
};