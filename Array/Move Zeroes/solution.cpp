class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left, right = 0;

        while(right < nums.size())
        {
            if (nums[right] != 0)
            {
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;
                left += 1;
                right += 1;
            }
            else
            {
                right += 1;
            }
        }
    }
};