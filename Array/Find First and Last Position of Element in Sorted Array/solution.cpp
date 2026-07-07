class Solution {
public:

    // Find first occurrence of target
    int findFirstElement(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;
        int result1 = -1; // default if target not found

        while(left <= right)
        {
            int mid = left + (right - left) / 2;

            if(nums[mid] == target)
            {
                result1 = mid;        // store possible answer
                right = mid - 1;      // keep searching on LEFT side
            }
            else if(nums[mid] < target)
            {
                left = mid + 1;       // move right
            }
            else
            {
                right = mid - 1;      // move left
            }
        }
        return result1;
    }


    // Find last occurrence of target
    int findLastElement(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;
        int result2 = -1;

        while(left <= right)
        {
            int mid = left + (right - left) / 2;

            if(nums[mid] == target)
            {
                result2 = mid;        // store index
                left = mid + 1;       // keep searching on RIGHT side
            }
            else if(nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        return result2;
    }

    vector<int> searchRange(vector<int>& nums, int target) 
    {
        return {findFirstElement(nums, target), findLastElement(nums, target)};
    }
};