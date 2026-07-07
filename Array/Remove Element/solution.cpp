class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
    int count = 0;

    for(int x = 0; x < nums.size(); ++x)
    {
        if (nums[x] != val)
        {
            nums[count] = nums[x];
            count += 1;
        }
    }
    return count;
    }
};