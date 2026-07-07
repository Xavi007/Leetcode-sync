class Solution {
public:
    int divide(int a, int b) {
        const int INT_MAX_VAL = 2147483647;   
        const int INT_MIN_VAL = -2147483648;
        
        if ((a == INT_MIN) && (b == -1))
        {
            return INT_MAX_VAL;
        }  
        else
        {
            return a/b;
        }
            
    }
};