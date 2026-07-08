class Solution {
public:
    bool isPowerOfTwo(int value) {
        if (value <= 0) return false;   
        return !(value & (value - 1));
    }
};