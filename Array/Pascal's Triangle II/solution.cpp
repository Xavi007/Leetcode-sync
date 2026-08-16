class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row = {1};

        for(int i = 1; i < rowIndex+1; ++i)
        {
            long long next_ele = (long long)row[i-1] * (rowIndex - i + 1) / i;
            row.push_back((int)next_ele);
        }
        return row;
    }
};