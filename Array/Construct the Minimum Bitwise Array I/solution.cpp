class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> final;
        for(int num : nums)
        {
            int bit_sum = -1;
            for(int x = 1; x<num; ++x)
            {
                if((x |( x + 1)) == num)
                {
                    bit_sum = x;
                    break;
                }
            } 
            final.push_back(bit_sum);
        }
        return final;
    }
};