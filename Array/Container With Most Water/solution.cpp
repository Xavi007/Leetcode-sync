class Solution {
public:
    int maxArea(vector<int>& height) 
    {
        int left = 0;
        int right = height.size() - 1;
        int max_storage = 0;


        while(left < right)
        {
            int min_water_avg = min(height[left], height[right]);
            int width_water = (right-left) * min_water_avg;
            max_storage = max(max_storage, width_water);

            if (height[left] < height[right])
            {
                left = left + 1;
            }
            else
            {
                right = right - 1;
            }
        }
        return max_storage;
    }
    
    
};