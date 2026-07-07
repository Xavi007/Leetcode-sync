class Solution {
public:
    bool canReach(vector<int>& arr, int idx) 
    {
        int end = arr.size();

        if(idx < 0 || idx >= end || arr[idx] < 0) {return false;}

        if(arr[idx] == 0){return true;}

        arr[idx] *= -1;
        bool a = canReach(arr, idx+arr[idx]);
        bool b = canReach(arr, idx-arr[idx]);

        return a || b;

    }
};